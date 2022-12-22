from flask import Flask
from config import Config
from flask_restful import Api
from flask_cors import CORS

# extensions
from app.extensions import db, ma, migrate, login_manager

# blueprints
from app.main import bp as main_bp

# app models
from app.models.users import User, UserToken
from app.models.todo import Todo

# api endpoints
from app.api.endpoints import UserEndpoint, TodoEndpoint, AllTodosEndpoint

# app factory
def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(config_class)

    
    CORS(app)
    api = Api(app)

    # initialize flask extensions
    db.init_app(app)
    ma.init_app(app)
    api.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # register app blueprints
    app.register_blueprint(main_bp)

    # register api endpoints
    api.add_resource(UserEndpoint, '/api/user/')
    api.add_resource(AllTodosEndpoint, '/api/todo/')
    api.add_resource(TodoEndpoint, '/api/todo/<task_id>/')

    # login manager callback
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    # return Flask instance
    return app