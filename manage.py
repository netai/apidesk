import os
from flask_migrate import Migrate
from flask_cors import CORS
from app import create_app, web_blueprint
from app.api import api_blueprint
from app.errors import error_blueprint
from app.extensions import db

app = create_app(os.getenv('ENV') or 'dev')
app.register_blueprint(web_blueprint)
app.register_blueprint(api_blueprint)
app.register_blueprint(error_blueprint)
app.app_context().push()
CORS(app, resources={r"/api/*": {"origins": "*"}})
migrate = Migrate(app, db)