import json


def test_tweet_new(app, client):
    payload = {
        "user_id": "1",
        "text": "😀😀😀😀"
    }
    res = client.post('/tweet/new', data=json.dumps(payload),
                      content_type='application/json')
    success = res.get_json()['success']
    assert success is True
    assert res.status_code == 200


def test_tweet_timeline(app, client):

    res = client.get('/tweet/timeline/1')
    success = res.get_json()['success']
    assert success is True
    assert res.status_code == 200
