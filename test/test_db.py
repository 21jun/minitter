import json


def test_post_fetch(app, client):
    res = client.get('/post/new')
    data = res.get_json()
    assert data['success'] is True
