from flask import Flask
from flask_cors import CORS

from ..config import config
from .extensions import init_extensions
from .routes.auth import bp as auth_bp
from .routes.tasks import bp as tasks_bp


def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    init_extensions(app)

    CORS(app, origins=['http://localhost:4200'])

    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)

    return app
