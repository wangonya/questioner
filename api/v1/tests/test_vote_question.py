from v1.tests import main, patch_json


def test_upvote_question(main):
    test_data = {}
    res = patch_json(main, '/api/v1/questions/1/upvote', test_data)
    assert res.status_code == 201 or res.status_code == 200


def test_downvote_question(main):
    test_data = {}
    res = patch_json(main, '/api/v1/questions/1/downvote', test_data)
    assert res.status_code == 201 or res.status_code == 200
