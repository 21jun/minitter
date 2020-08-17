import json


def test_sign_up_success(app, client):
    payload = {
        "name": "TEST",
        "email": "test@email.com",
        "password": "111",
        "profile": "Hi There!"
    }
    res = client.post('/auth/sign-up', data=json.dumps(payload),
                      content_type='application/json')
    data = res.get_json()['data']

    assert str(data['name']) == "TEST"
    assert res.status_code == 200


def test_sign_up_fail(app, client):

    # No password passed
    payload = {
        "name": "TEST",
        "profile": "Hi There!"
    }
    res = client.post('/auth/sign-up', data=json.dumps(payload),
                      content_type='application/json')

    assert res.status_code == 400


def test_login(app, client):
    payload = {
        "email": "test@email.com",
        "password": "111",
    }
    res = client.post('/auth/login', data=json.dumps(payload),
                      content_type='application/json')

    assert res.status_code == 200
