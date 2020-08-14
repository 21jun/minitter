import json


def test_tweet_timeline(app, client):
    res = client.get('/tweet/timeline/1')
    data = res.get_json()

    assert data['success'] is True
