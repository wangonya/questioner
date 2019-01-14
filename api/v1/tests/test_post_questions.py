from api.v1.tests import main, post_json


def test_post_question(main):
    test_data = {
        "title": "sample question",
        "body": "sample question body",
        "meetup": 1
    }
    res = post_json(main, '/api/v1/questions', test_data)
    assert res.status_code == 201
