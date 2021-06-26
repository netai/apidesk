from flask import Flask
from flask import Blueprint
from .routes import api_routes

api_blueprint = Blueprint('api', __name__, url_prefix='/api')
api_routes(api_blueprint)