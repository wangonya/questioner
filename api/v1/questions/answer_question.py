from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity

from ..questions.models import PostQuestionsModel, AnswerQuestionsModel
from ..auth.models import AuthModel
from ..utils.validators import AnswerValidators


class AnswerQuestion(Resource):
    """post answer endpoint resource"""
    parser = reqparse.RequestParser()
    parser.add_argument("body",
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")

    @jwt_required
    def post(self, q_id):
        """do a POST on the answers endpoint"""
        data = AnswerQuestion.parser.parse_args()
        body = data["body"]

        # get current user from jwt token
        user = get_jwt_identity()
        creator = AuthModel.find_by_uid(user)

        meetup = PostQuestionsModel.find_meetup_by_q_id(q_id)

        # handle duplicates
        AnswerValidators.check_duplicate_answer(body, q_id)

        answer = AnswerQuestionsModel(body, creator, meetup, q_id)
        answer.save_answer_to_db()

        response = {
            "status": 201,
            "message": "answer submitted successfully",
            "data": [{
                "body": body,
                "creator": creator,
                "meetup": meetup,
                "for_question": q_id
            }]}

        return response, 201
