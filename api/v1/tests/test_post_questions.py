from v1.tests import main, post_json


def test_post_question(main):
    test_data = {
        "id": 1,
        "createdOn": "some date",
        "createdBy": 1,
        "meetup": 1,
        "title": "sample question",
        "body": "sample question body",
        "votes": 0
    }
    res = post_json(main, '/api/v1/questions', test_data)
    assert res.status_code == 201
