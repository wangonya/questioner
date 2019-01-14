from api.v1.tests import main, post_json


def test_post_meetup(main):
    test_data = {
            "title": "sample meetup",
            "location": "test location",
            "happening_on": "test date",
            "tags": ["tag1", "tag2", "tag3"],
            "image": ""
        }
    res = post_json(main, '/api/v1/meetups', test_data)
    assert res.status_code == 201 or res.status_code == 401
    assert b"meetup created successfully" in res.data or b"Only admins can access this route" in res.data
