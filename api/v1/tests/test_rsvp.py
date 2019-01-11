from api.v1.tests import main, post_json


def test_rsvp_meetup(main):
    test_data = {
            "status": "maybe"
        }
    res = post_json(main, '/api/v1/meetups/1/rsvps', test_data)
    assert res.status_code == 201 or res.status_code == 200
