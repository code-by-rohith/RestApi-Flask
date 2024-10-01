from flask import Blueprint

arithmetic_bp = Blueprint('arithmetic', __name__)

from . import routes
