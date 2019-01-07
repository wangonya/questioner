from v1.tests import main, post_json


def test_sign_up_valid(main):
    test_data = {
        'email': 'kwangonya@gmail.com',
        'password': 'test_pass!'
    }
    res = post_json(main, '/api/v1/auth/signup', test_data)
    assert res.status_code == 201


def test_sign_up_invalid_email(main):
    test_data = {
        'email': 'kwangonyagmail.com',
        'password': 'test_pass!'
    }
    res = post_json(main, '/api/v1/auth/signup', test_data)
    assert res.status_code == 400


def test_sign_up_invalid_password(main):
    test_data = {
        'email': 'kwangonya@gmail.com',
        'password': 'test!'
    }
    res = post_json(main, '/api/v1/auth/signup', test_data)
    assert res.status_code == 422
