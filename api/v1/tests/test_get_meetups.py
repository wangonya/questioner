from api.v1.tests import main


def test_get_no_upcoming_meetups(main):
    res = main.get('/api/v1/meetups/upcoming')
    assert res.status_code == 200


def test_no_specific_meetup(main):
    res = main.get('/api/v1/meetups/54')
    assert res.status_code == 404


def test_specific_meetup(main):
    res = main.get('/api/v1/meetups/1')
    assert res.status_code == 200 or res.status_code == 404


def test_admin_meetup(main):
    res = main.get('/api/v1/admin/profile/1')
    assert res.status_code == 200 or res.status_code == 401


