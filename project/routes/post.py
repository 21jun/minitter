import json
from datetime import datetime
from flask import Blueprint, jsonify
from project.models.users import User
from project.models.posts import Post
from project.models import db

posts_bp = Blueprint('post', __name__, url_prefix='/post')


@posts_bp.route('/')
def index():
    return "post index"


@posts_bp.route('/new')
def first_post():

    title = "Hello World"
    content = "This is the new world"
    create_date = datetime.now()
    post = Post(title=title, content=content, create_date=create_date)
    db.session.add(post)
    db.session.commit()

    all_post = db.session.query(Post).order_by(Post.create_date.desc()).all()

    posts = []
    for post in all_post:
        posts.append(
            {
                "id": post.id,
                "title": post.title,
                "content": post.content,
                "create_date": post.create_date
            }
        )

    response = {
        'success': True,
        'data': posts,
        'msg': ""
    }

    return jsonify(response)


@posts_bp.route('/view')
def view_post():

    all_post = db.session.query(Post).order_by(Post.create_date.desc()).all()

    posts = []
    for post in all_post:
        posts.append(
            {
                "id": post.id,
                "title": post.title,
                "content": post.content,
                "create_date": post.create_date
            }
        )

    response = {
        'success': True,
        'data': posts,
        'msg': ""
    }

    return jsonify(response)
