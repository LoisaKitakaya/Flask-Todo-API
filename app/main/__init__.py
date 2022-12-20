from flask import Blueprint
from app.extensions import login_manager

bp = Blueprint('main', __name__)

from . import routes

login_manager.login_view = 'main.login'
login_manager.login_message_category = "info"