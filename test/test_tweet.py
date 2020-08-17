import json


def test_tweet_new(app, client):

    # Sign Up
    new_user = {
        "name": "Tweet",
        "password": "1qazxc",
        "email": "tweet@gmail.com",
        "profile": "🍕🍕🍕"
    }

    res = client.post('/auth/sign-up', data=json.dumps(new_user),
                      content_type='application/json')
    assert res.status_code == 200

    login_info = {
        "password": "1qazxc",
        "email": "tweet@gmail.com"
    }
    res = client.post('/auth/login', data=json.dumps(login_info),
                      content_type='application/json')

    res_json = json.loads(res.data.decode())
    access_token = res_json['access_token']

    assert res.status_code == 200

    # Tweet
    tweet = {"text": "Hi~"}
    res = client.post('/tweet/new', data=json.dumps(tweet),
                      headers={'Authorization': access_token},
                      content_type='application/json')

    assert res.status_code == 200
    over300bytes = """
        🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
        🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠
        🌌🌌🌌🌌🌌🌌🌌🌌🌌🌌
        🍻🍻🍻🍻🍻🍻🍻🍻🍻🍻
        🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨
        🥝🥝🥝🥝🥝🥝🥝🥝🥝🥝
        🌏🌏🌏🌏🌏🌏🌏🌏🌏🌏🌏
        🌝🌝🌝🌝🌝🌝🌝🌝🌝🌝
        🐣🐣🐣🐣🐣🐣🐣🐣🐣🐣🐣
        👩🏿‍💻👩🏿‍💻👩🏿‍💻👩🏿‍💻👩🏿‍💻👩🏿‍💻👩🏿‍💻👩🏿‍💻👩🏿‍💻👩🏿‍💻
        ⚙️⚙️⚙️⚙️⚙️⚙️⚙️⚙️⚙️⚙️⚙️⚙️⚙️⚙️⚙️⚙️⚙️⚙️⚙️⚙️⚙️⚙️⚙️
        🧸🧸🧸🧸🧸🧸🧸🧸🧸🧸🧸
        💰💰💰💰💰💰💰💰💰💰💰💰
        💎💎💎💎💎💎💎💎💎💎💎
    """

    tweet = {"text": over300bytes}
    res = client.post('/tweet/new', data=json.dumps(tweet),
                      headers={'Authorization': access_token},
                      content_type='application/json')

    assert res.status_code == 400


def test_tweet_timeline(app, client):

    res = client.get('/tweet/timeline/1')
    success = res.get_json()['success']
    # print(res.get_json()['data'])
    assert success is True
    assert res.status_code == 200
