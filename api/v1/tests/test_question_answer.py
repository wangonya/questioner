from api.v1.tests import main, post_json, new_answer


def test_answer_question(main, new_answer):
    test_data = {
        "id": 1,
        "body": "sample answer body",
        "creator": 1,
        "meetup": 1,
        "for_question": 1
    }
    res = post_json(main, '/api/v1/questions/1/answer', test_data)
    assert isinstance(new_answer.a_id, int)
    assert new_answer.body == "sample answer body"
    assert isinstance(new_answer.creator, int)
    assert isinstance(new_answer.meetup, int)
    assert res.status_code == 201
    assert b"answer submitted successfully" in res.data
