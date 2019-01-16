from api.v1.tests import main, post_json, new_rsvp


def test_rsvp_meetup(main, new_rsvp):
    test_data = {
            "status": "yes"
        }
    assert isinstance(new_rsvp.rsvp_id, int)
    assert new_rsvp.status == "yes"
    assert isinstance(new_rsvp.uid, int)
    assert isinstance(new_rsvp.m_id, int)
    res = post_json(main, '/api/v1/meetups/1/rsvps', test_data)
    assert res.status_code == 201 or res.status_code == 200
