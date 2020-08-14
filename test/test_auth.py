import json


def test_sign_up(app, client):
    res = client.post('/auth/sign-up', data=json.dumps({"name": "Lee"}),
                      content_type='application/json')
    data = res.get_json()
    assert str(data['name']) == "Lee"
