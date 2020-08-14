from flask import Blueprint, jsonify, request
from datetime import datetime

tweet_bp = Blueprint('tweet', __name__, url_prefix='/tweet')


@tweet_bp.route('/new', methods=['POST'])
def new_tweet():
    payload = request.get_json()
    user_id = int(payload['id'])
    tweet = payload['tweet']

    if len(tweet) > 300:
        return "Limit 300 bytes", 400

    return jsonify({
        "tweet": tweet,
        "user_id": user_id,
        "datetime": datetime.now(),
        "success": True
    })
