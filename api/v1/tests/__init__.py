import pytest
import json
from flask_jwt_extended import create_access_token
import api

from ..auth.models import AuthModel
from ..meetups.models import MeetupModel, RsvpsModel
from ..questions.models import PostQuestionsModel, AnswerQuestionsModel, VoteModel
# manually push app context
# to avoid working outside of application context
ctx = api.create_app().test_request_context()
ctx.push()
access_token = create_access_token('kwangonya@gmail.com')
headers = {'Authorization': 'Bearer {}'.format(access_token)}
ctx.pop()


@pytest.fixture
def main():
    main = api.create_app()
    return main.test_client()


@pytest.fixture
def new_user():
    user = AuthModel('fname', 'lname', 'kwangonya@gmail.com', '23432432', 'test_pass!')
    return user


@pytest.fixture
def new_meetup():
    meetup = MeetupModel('sample meetup', 1, 'test location', 'test date', ["tag1", "tag2", "tag3"], "")
    return meetup


@pytest.fixture
def new_rsvp():
    rsvp = RsvpsModel('yes', 1, 1)
    return rsvp


@pytest.fixture
def new_question():
    question = PostQuestionsModel('sample question', 1, 'sample question body', 1)
    return question


@pytest.fixture
def new_answer():
    answer = AnswerQuestionsModel('sample answer body', 1, 1, 1)
    return answer


@pytest.fixture
def new_upvote():
    upvote = VoteModel.save_upvote_to_db(1, 1)
    return upvote


@pytest.fixture
def new_downvote():
    downvote = VoteModel.save_downvote_to_db(1, 1)
    return downvote


def post_json(main, url, json_dict):
    return main.post(url, data=json.dumps(json_dict), content_type='application/json', headers=headers)


def patch_json(main, url, json_dict):
    return main.patch(url, data=json.dumps(json_dict), content_type='application/json', headers=headers)
