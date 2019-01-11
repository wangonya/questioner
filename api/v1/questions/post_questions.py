from flask import request, abort, jsonify, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
import datetime as date
from api.v1.questions import models
from api.v1.auth.models import users
from api.v1.meetups.models import meetups

post_q = Blueprint('post_q', __name__, url_prefix='/api/v1')


@post_q.route('/questions', methods=['POST'])
@jwt_required
def post_question():

    try:
        title = request.json['title']
        body = request.json['body']
        meetup = request.json['meetup']

        # check if the meetup exists
        if not any(m['id'] == meetup for m in meetups):
            return jsonify(
                {
                    "status": 404,
                    "error": "meetup with id {} does not exist".format(meetup)
                }), 404

        try:
            q_id = models.questions[-1]['id'] + 1
        except IndexError:
            q_id = 1

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

        question = {
            "id": q_id,
            "title": title,
            "body": body,
            "createdBy": userid,
            "meetup": meetup,
            "votes": 0,
            "createdOn": date.datetime.now()
        }
        models.questions.append(question)
        return jsonify(
            {
                "status": 201,
                "data": [{
                    "id": q_id,
                    "msg": "question added successfully",
                    "title": title,
                    "body": body,
                    "user": userid,
                    "meetup": meetup
                }]
            }
        ), 201
    except (ValueError, KeyError, TypeError):
        abort(400)
