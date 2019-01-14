from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity

from ..questions.models import PostQuestionsModel
from ..auth.models import AuthModel
from ..meetups.models import MeetupModel


class PostQuestion(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("title",
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")
    parser.add_argument("body",
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")
    parser.add_argument("meetup",
                        type=int,
                        required=True,
                        help="This field cannot be left blank!")

    @jwt_required
    def post(self):
        data = PostQuestion.parser.parse_args()
        title = data["title"]
        body = data["body"]
        meetup = data["meetup"]

        # get current user from jwt token
        user = get_jwt_identity()
        creator = AuthModel.find_by_uid(user)

        MeetupModel.find_by_m_id(meetup)

        question = PostQuestionsModel(title, creator, body, meetup)
        question.save_question_to_db()

        response = {
            "status": 201,
            "message": "question submitted successfully",
            "data": [{
                "title": title,
                "body": body,
                "creator": creator,
                "meetup": meetup
            }]}

        return response, 201
