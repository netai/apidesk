from flask import Flask
from flask import Blueprint

error_blueprint = Blueprint('errors', __name__, template_folder='templates', static_folder='static', url_prefix='/')

from app.errors import handlers