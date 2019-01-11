from api.v1.tests import main, post_json


def test_answer_question(main):
    test_data = {
        "id": 1,
        "createdOn": "some date",
        "createdBy": 1,
        "meetup": 1,
        "body": "sample answer body",
        "forQuestion": 1
    }
    res = post_json(main, '/api/v1/questions/1/answer', test_data)
    assert res.status_code == 201
