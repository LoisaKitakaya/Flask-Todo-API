from flask import Flask
from config import Config

# blueprints
from app.tokens import bp as token_bp

# app factory

def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(config_class)

    # initialize flask extensions

    # register app blueprints
    app.register_blueprint(token_bp)

    return app