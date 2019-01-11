from api.v1.tests import main, post_json


def test_post_meetup(main):
    test_data = {
            "title": "sample meetup",
            "location": "test location",
            "happeningOn": "test date",
            "tags": ["tag1", "tag2", "tag3"],
            "image": ""
        }
    res = post_json(main, '/api/v1/meetups', test_data)
    assert res.status_code == 201 or res.status_code == 401
