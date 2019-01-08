from flask import jsonify, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from v1.questions import models
from v1.auth.models import users

upvote_q = Blueprint('upvote_q', __name__, url_prefix='/api/v1')


@upvote_q.route('/questions/<int:q_id>/upvote', methods=['PATCH'])
@jwt_required
def upvote_question(q_id):
    # get a list of the question object with the matching question-id
    # and retrieve the meetup info from it
    try:
        meetup = [q for q in models.questions if q['id'] == q_id][0]['meetup']
        title = [q for q in models.questions if q['id'] == q_id][0]['title']
        body = [q for q in models.questions if q['id'] == q_id][0]['body']
    except IndexError:
        return jsonify(
            {
                "status": 500,
                "error": "error retrieving meetup"
            }), 500

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

    upvote = {
        "user": userid,
        "question": q_id,
        "count": 1
    }

    # check if user has already voted
    # if they have, remove the record
    # if not, append
    if any(u['user'] == userid and u['question'] == q_id for u in models.votes):
        models.votes.remove(upvote)
        return jsonify(
            {
                "status": 200,
                "data": [{
                    "msg": "vote removed",
                    "title": title,
                    "body": body,
                    "meetup": meetup,
                    "votes": sum(s['count'] for s in models.votes)
                }]
            }), 200
    else:
        models.votes.append(upvote)
        return jsonify(
            {
                "status": 201,
                "data": [{
                    "msg": "vote added successfully",
                    "title": title,
                    "body": body,
                    "meetup": meetup,
                    "votes": sum(s['count'] for s in models.votes)
                }]
            }
        ), 201
