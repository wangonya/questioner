import datetime

from api.v1.tests import main, post_json, new_question


def test_post_question(main, new_question):
    test_data = {
        "title": "sample question",
        "body": "sample question body",
        "meetup": 1
    }
    res = post_json(main, '/api/v1/meetups/1/questions', test_data)
    assert isinstance(new_question.q_id, int)
    assert new_question.title == "sample question"
    assert isinstance(new_question.creator, int)
    assert new_question.body == "sample question body"
    assert isinstance(new_question.meetup, int)
    assert isinstance(new_question.created_on, datetime.datetime)
    assert isinstance(new_question.meetup, int)
    assert res.status_code == 201
    assert b"question submitted successfully" in res.data
