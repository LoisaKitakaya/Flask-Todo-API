from flask import Flask
from config import Config

# app factory

def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(config_class)

    # initialize flask extensions

    # register app blueprints

    return app