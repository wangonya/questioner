from api.v1.tests import main, patch_json, new_upvote, new_downvote


def test_upvote_question(main, new_upvote):
    test_data = {}
    res = patch_json(main, '/api/v1/questions/1/upvote', test_data)
    assert res.status_code == 201
    assert isinstance(new_upvote, int)
    assert b"vote added successfully" in res.data


def test_downvote_question(main, new_downvote):
    test_data = {}
    res = patch_json(main, '/api/v1/questions/1/downvote', test_data)
    assert res.status_code == 201
    assert isinstance(new_downvote, int)
    assert b"vote added successfully" in res.data
