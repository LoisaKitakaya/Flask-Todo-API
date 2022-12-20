from flask import Flask
from config import Config

# extensions
from app.extensions import db, migrate

# blueprints
from app.main import bp as main_bp
from app.docs import bp as docs_bp
from app.tokens import bp as tokens_bp

# app models
from app.models.users import User
from app.models.todo import Todo

# app factory

def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(config_class)

    # initialize flask extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # register app blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(docs_bp)
    app.register_blueprint(tokens_bp)

    return app