from flask import Flask
from config import Config

# blueprints
from app.main import bp as main_bp

# app factory

def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(config_class)

    # initialize flask extensions

    # register app blueprints
    app.register_blueprint(main_bp)

    return app