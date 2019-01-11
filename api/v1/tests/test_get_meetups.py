from api.v1.tests import main


def test_get_upcoming_meetups(main):
    res = main.get('/api/v1/meetups/upcoming')
    assert res.status_code == 200


def test_specific_meetup(main):
    res = main.get('/api/v1/meetups/1')
    assert res.status_code == 200
