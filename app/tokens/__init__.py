from flask import Blueprint

bp = Blueprint('tokens', __name__)

from . import routes