from flask import request, Response
from flask import g, current_app
from project.models.users import User
from project.models import db
import jwt
from functools import wraps

HASH_ALG = ['HS256']


def get_user_info(user_id):
    user = db.session.query(User).filter(User.id == user_id).one()

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "profile": user.profile
    }


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        access_token = request.headers.get("Authorization", None)
        if access_token is not None:
            try:
                payload = jwt.decode(
                    access_token, current_app.config['JWT_SECRET_KEY'], algorithms=HASH_ALG)
            except jwt.InvalidTokenError:
                payload = None

            if payload is None:
                return Response(status=401)

            user_id = payload['user_id']
            g.user_id = user_id
            g.user = get_user_info(user_id) if user_id else None
        else:
            return Response(status=401)

        return f(*args, **kwargs)
    return decorated_function
