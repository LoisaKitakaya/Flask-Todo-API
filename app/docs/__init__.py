from flask import Blueprint

bp = Blueprint('docs', __name__)

from . import routes