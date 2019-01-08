from v1.tests import main


def test_get_questions(main):
    res = main.get('/api/v1/meetups/upcoming')
    assert res.status_code == 200
