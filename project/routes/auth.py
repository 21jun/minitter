from flask import Blueprint, jsonify, request
from random import randint

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/sign-up', methods=['POST'])
def sign_up():
    new_user = request.get_json()
    print(new_user)
    new_user['id'] = randint(1, 1000)
    return jsonify(new_user)
