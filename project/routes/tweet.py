import re
from flask import Blueprint, jsonify, request
from flask import g
from project.models.tweet import Tweet
from project.models.users import User
from project.models import db
from datetime import datetime
from project.login.login import login_required

tweet_bp = Blueprint('tweet', __name__, url_prefix='/tweet')


@tweet_bp.route('/new', methods=['POST'])
@login_required
def new_tweet():
    payload = request.get_json()

    response = {
        'success': True,
        'data': None,
        'msg': ""
    }

    new_tweet = {
        'text': payload.get('text', None),
        'user_id': g.get('user_id', None),
        "created_at": datetime.now()
    }

    if any(value == None for value in new_tweet.values()):
        response['success'] = False
        response['msg'] = "There are missing values in tweet/new form"
        return jsonify(response), 400

    if len(new_tweet['text']) > 300:
        response['success'] = False
        response['msg'] = "Limit tweet message upto 300 bytes"
        return jsonify(response), 400

    tweet = Tweet(**new_tweet)

    db.session.add(tweet)
    db.session.commit()

    response['data'] = new_tweet

    return jsonify(response), 200


@tweet_bp.route('/timeline/<int:user_id>', methods=['GET'])
def timeline(user_id):

    response = {
        'success': True,
        'data': None,
        'msg': ""
    }

    tweets = db.session.query(Tweet, User).join(
        User, Tweet.user_id == User.id).order_by(Tweet.created_at.desc()).all()

    data = [{
        "user_id": user.id,
        "user_name": user.name,
        "text": tweet.text,
        "created_at": tweet.created_at
    } for tweet, user in tweets]

    if data == []:
        response['success'] = False
        response['msg'] = "No Tweets Available"
        return jsonify(response), 400

    response['data'] = data
    return jsonify(response), 200
