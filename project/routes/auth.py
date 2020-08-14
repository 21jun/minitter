from datetime import datetime
from flask import Blueprint, jsonify, request
from project.models.users import User
from project.models import db

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/sign-up', methods=['POST'])
def sign_up():

    new_user = request.get_json()
    print(new_user)

    new_user = {
        "hashed_password": new_user.get("password", None),
        "name": new_user.get("name", "default_user_name"),
        "email": new_user.get("email", "defualt_user_email"),
        "profile": new_user.get("profile", ""),
        "created_at": datetime.now()
    }

    # TODO: hash password
    user = User(**new_user)

    db.session.add(user)
    db.session.commit()

    return jsonify(new_user)
