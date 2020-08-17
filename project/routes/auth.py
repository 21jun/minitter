from datetime import datetime, timedelta
from flask import Blueprint, jsonify, request, current_app

from project.models.users import User
from project.models import db
from sqlalchemy.orm.exc import NoResultFound
import jwt
import bcrypt


auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

HASH_ALG = ['HS256']


def check_password(raw_pw):
    if 8 > len(raw_pw) < 20:
        return False


@auth_bp.route('/login', methods=['POST'])
def login():

    credential = request.get_json()

    response = {
        'success': True,
        'msg': ""
    }

    email = credential.get('email', None)
    raw_pw = credential.get('password', None)

    try:
        user = db.session.query(User).filter(User.email == email).one()
    except NoResultFound:
        response['success'] = False
        response['msg'] = "No User Found"
        return jsonify(response), 401

    if not bcrypt.checkpw(raw_pw.encode('UTF-8'), user.hashed_password):
        response['success'] = False
        response['msg'] = "Incorrect Password"
        return jsonify(response), 401

    # Login Success
    payload = {
        "user_id": user.id,
        "exp": datetime.utcnow() + timedelta(seconds=60*60*24)
    }
    token = jwt.encode(payload, current_app.config['JWT_SECRET_KEY'], 'HS256')

    response['access_token'] = token.decode('UTF-8')

    return jsonify(response)


@auth_bp.route('/sign-up', methods=['POST'])
def sign_up():

    new_user = request.get_json()

    response = {
        'success': True,
        'data': None,
        'msg': ""
    }

    raw_pw = new_user.get("password", None)
    if raw_pw is not None:
        hashed_pw = bcrypt.hashpw(raw_pw.encode('UTF-8'), bcrypt.gensalt())
    else:
        return jsonify(response), 400

    new_user_data = {
        "hashed_password": hashed_pw,
        "name": new_user.get("name", "default_user_name"),
        "email": new_user.get("email", "defualt_user_email"),
        "profile": new_user.get("profile", ""),
        "created_at": datetime.now()
    }

    if any(value == None for value in new_user_data.values()):
        response['success'] = False
        response['msg'] = "There are missing values in sing-up form"
        return jsonify(response), 400

    user = User(**new_user_data)

    try:
        isdup = db.session.query(User).filter(User.email == user.email).one()
    except NoResultFound:
        isdup = None

    if isdup:
        return "User Email Already Exists.", 400

    db.session.add(user)
    db.session.commit()

    new_user_data.pop("hashed_password")
    response['data'] = new_user_data
    return jsonify(response), 200
