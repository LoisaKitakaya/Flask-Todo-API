from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_restful import Api
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
api = Api()
ma = Marshmallow()