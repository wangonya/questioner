import datetime

from api.v1.tests import main, post_json, new_user


def test_sign_up_valid(main, new_user):
    test_data = {
        "firstname": "fname",
        "lastname": "lname",
        "email": "kwangonya@gmail.com",
        "phonenumber": "23432432",
        "password": "test_pass!"
    }
    assert isinstance(new_user.uid, int)
    assert new_user.firstname == "fname"
    assert new_user.lastname == "lname"
    assert new_user.email == "kwangonya@gmail.com"
    assert new_user.phonenumber == "23432432"
    assert new_user.password != "test_pass!"
    assert isinstance(new_user.registered, datetime.datetime)
    res = post_json(main, "/api/v1/auth/signup", test_data)
    assert res.status_code == 201
    assert b"user registered successfully" in res.data


def test_sign_up_invalid_email(main):
    test_data = {
        "email": "kwangonyagmail.com",
        "password": "test_pass!",
        "firstname": "fname",
        "lastname": "lname",
        "phonenumber": "878878786"
    }
    res = post_json(main, "/api/v1/auth/signup", test_data)
    assert res.status_code == 400
    assert b"Invalid email format" in res.data


def test_sign_up_invalid_password(main):
    test_data = {
        "email": "kwangony@gmail.com",
        "password": "test!",
        "firstname": "fname",
        "lastname": "lname",
        "phonenumber": "878878786"
    }
    res = post_json(main, "/api/v1/auth/signup", test_data)
    assert res.status_code == 400
    assert b"Invalid password length" in res.data


def test_log_in_valid(main):
    test_data = {
        "email": "kwangonya@gmail.com",
        "password": "test_pass!"
    }
    res = post_json(main, "/api/v1/auth/login", test_data)
    assert res.status_code == 200
    assert b"user logged in successfully" in res.data


def test_log_in_invalid_email(main):
    test_data = {
        "email": "kwangonyagmail.com",
        "password": "test_pass!"
    }
    res = post_json(main, "/api/v1/auth/login", test_data)
    assert res.status_code == 400
    assert b"Invalid email format" in res.data


def test_log_in_invalid_password(main):
    test_data = {
        "email": "kwangony@gmail.com",
        "password": "test!"
    }
    res = post_json(main, "/api/v1/auth/login", test_data)
    assert res.status_code == 401
    assert b"Incorrect login details" in res.data


def test_reset_valid(main):
    test_data = {
        "email": "kwangonya@gmail.com"
    }
    res = post_json(main, "/api/v1/auth/reset", test_data)
    assert res.status_code == 200
    assert b"password reset instructions have been sent to your email" in res.data


def test_reset_invalid_email(main):
    test_data = {
        "email": "kwangonyagmail.com"
    }
    res = post_json(main, "/api/v1/auth/reset", test_data)
    assert res.status_code == 400
    assert b"Invalid email format" in res.data


def test_reset_invalid(main):
    test_data = {
        "email": "kwango@gmail.com"
    }
    res = post_json(main, "/api/v1/auth/reset", test_data)
    assert res.status_code == 404
    assert b"No data exists in the requested resource" in res.data
