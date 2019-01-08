from v1.tests import main, patch_json


def test_post_question(main):
    test_data = {}
    res = patch_json(main, '/api/v1/questions/<int:q_id>/upvote', test_data)
    assert res.status_code == 201 or 200
