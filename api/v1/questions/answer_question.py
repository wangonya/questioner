from flask import request, abort, jsonify, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
import datetime as date
from api.v1.questions import models
from api.v1.auth.models import users
from api.v1.meetups.models import meetups

answer_q = Blueprint('answer_q', __name__, url_prefix='/api/v1')


@answer_q.route('/questions/<int:q_id>/answer', methods=['POST'])
@jwt_required
def answer_question(q_id):

    try:
        # check if the question exists
        if not any(q['id'] == q_id for q in models.questions):
            return jsonify(
                {
                    "status": 404,
                    "error": "question with id {} does not exist".format(q_id)
                }), 404

        body = request.json['body']
        meetup = [q for q in models.questions if q['id'] == q_id][0]['meetup']

        try:
            a_id = models.answers[-1]['id'] + 1
        except IndexError:
            a_id = 1

        # get current user from jwt token
        user = get_jwt_identity()

        # get a list of the user object with the matching email retrieved from get_jwt_identity()
        # and retrieve the user id from it
        try:
            userid = [u for u in users if u['email'] == user][0]['id']
        except IndexError:
            return jsonify(
                {
                    "status": 500,
                    "error": "error retrieving user"
                }), 500

        answer = {
            "id": a_id,
            "body": body,
            "createdBy": userid,
            "meetup": meetup,
            "createdOn": date.datetime.now(),
            "forQuestion": q_id
        }
        models.answers.append(answer)
        return jsonify(
            {
                "status": 201,
                "data": [{
                    "id": a_id,
                    "msg": "answer added successfully",
                    "body": body,
                    "user": userid,
                    "meetup": meetup,
                    "forQuestion": q_id
                }]
            }
        ), 201
    except (ValueError, KeyError, TypeError):
        abort(400)
