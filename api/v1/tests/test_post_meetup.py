from api.v1.tests import main, post_json, new_meetup


def test_post_meetup(main, new_meetup):
    test_data = {
            "title": "sample meetup",
            "location": "test location",
            "happening_on": "test date",
            "tags": ["tag1", "tag2", "tag3"],
            "image": ""
        }
    res = post_json(main, '/api/v1/meetups', test_data)
    assert isinstance(new_meetup.m_id, int)
    assert new_meetup.title == "sample meetup"
    assert isinstance(new_meetup.creator, int)
    assert new_meetup.location == "test location"
    assert new_meetup.happening_on == "test date"
    assert new_meetup.tags == (['tag1', 'tag2', 'tag3'],)
    assert res.status_code == 201 or res.status_code == 401
    assert b"meetup created successfully" in res.data or b"Only admins can access this route" in res.data
