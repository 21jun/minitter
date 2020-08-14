from flask import Blueprint

index_bp = Blueprint('index', __name__, url_prefix='/')


@index_bp.route('/')
def index():
    return "Home"
