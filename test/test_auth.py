import json


def test_sign_up(app, client):
    payload = {
        "name": "Lee",
        "password": "111",
        "profile": "Hi There!"
    }
    res = client.post('/auth/sign-up', data=json.dumps(payload),
                      content_type='application/json')
    data = res.get_json()

    assert str(data['name']) == "Lee"


def test_login(app, client):
    pass
