from flask import Flask
from .config import Config
from .blueprints.main import main_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register blueprints (we'll add auth, admin, scholarships, etc. here)
    app.register_blueprint(main_bp)

    return app