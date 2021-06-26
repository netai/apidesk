from flask import render_template, request
from app import db
from app.errors import error_blueprint
from app.api.errors import error_response as api_error_response

def wants_json_response():
    return request.accept_mimetypes['application/json'] >= \
        request.accept_mimetypes['text/html']

@error_blueprint.app_errorhandler(404)
def not_found_error(error):
    if wants_json_response():
        return api_error_response(404, 'The page is not exist for the requested URL')
    return render_template('errors/404.html'), 404

@error_blueprint.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    if wants_json_response():
        return api_error_response(500, 'An unexpected error has occurred')
    return render_template('errors/500.html'), 500

@error_blueprint.app_errorhandler(405)
def method_not_allowed_error(error):
    db.session.rollback()
    if wants_json_response():
        return api_error_response(405, 'The method is not allowed for the requested URL')
    return render_template('errors/405.html'), 405