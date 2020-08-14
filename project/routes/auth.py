from datetime import datetime
from flask import Blueprint, jsonify, request
from project.models.users import User
from project.models import db

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/sign-up', methods=['POST'])
def sign_up():

    print(request.__dict__)

    new_user = request.get_json()
    print(new_user)

    id = new_user.get("id", None)
    pw = new_user.get("password", None)
    name = new_user.get("name", "default_user_name")
    email = new_user.get("email", "defualt_user_email")
    profile = new_user.get("profile", "")
    created_at = datetime.now()

    # TODO: hash password
    user = User(id=id, hashed_password=pw, name=name, email=email,
                profile=profile, created_at=created_at)

    # user = User(**new_user)???
    print(id, pw, profile)

    db.session.add(user)
    db.session.commit()

    return jsonify(new_user)
