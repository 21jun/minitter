import json


def test_sign_up_success(app, client):
    payload = {
        "name": "Lee",
        "password": "111",
        "profile": "Hi There!"
    }
    res = client.post('/auth/sign-up', data=json.dumps(payload),
                      content_type='application/json')
    data = res.get_json()['data']

    assert str(data['name']) == "Lee"


def test_sign_up_fail(app, client):

    # No password passed
    payload = {
        "name": "Lee",
        "profile": "Hi There!"
    }
    res = client.post('/auth/sign-up', data=json.dumps(payload),
                      content_type='application/json')
    success = res.get_json()['success']

    assert success == False


def test_login(app, client):
    pass
