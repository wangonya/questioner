from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from ..questions.models import VoteModel, PostQuestionsModel
from ..auth.models import AuthModel


class Upvote(Resource):
    @jwt_required
    def post(self, q_id):
        meetup = PostQuestionsModel.find_meetup_by_q_id(q_id)
        title = PostQuestionsModel.find_title_by_q_id(q_id)
        body = PostQuestionsModel.find_body_by_q_id(q_id)
        user = get_jwt_identity()
        voter = AuthModel.find_by_uid(user)

        votes = VoteModel.save_upvote_to_db(voter, q_id)

        response = {
            "status": 201,
            "message": "vote added successfully",
            "data": [{
                "title": title,
                "body": body,
                "meetup": meetup,
                "votes": votes
            }]
        }

        return response, 201


class DownVote(Resource):
    @jwt_required
    def post(self, q_id):
        meetup = PostQuestionsModel.find_meetup_by_q_id(q_id)
        title = PostQuestionsModel.find_title_by_q_id(q_id)
        body = PostQuestionsModel.find_body_by_q_id(q_id)
        user = get_jwt_identity()
        voter = AuthModel.find_by_uid(user)

        votes = VoteModel.save_downvote_to_db(voter, q_id)

        response = {
            "status": 201,
            "message": "vote added successfully",
            "data": [{
                "title": title,
                "body": body,
                "meetup": meetup,
                "votes": votes
            }]
        }

        return response, 201

