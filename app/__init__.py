from flask import Flask
from flask import Blueprint
from .routes import web_routes
from .environment import env
from .extensions import db, bcrypt

web_blueprint = Blueprint('app', __name__, template_folder='templates', static_folder='static', url_prefix='/')
web_routes(web_blueprint)

def create_app(env_name):
    app = Flask(__name__)
    app.config.from_object(env[env_name])
    db.init_app(app)
    bcrypt.init_app(app)
    return app
