from flask import request, abort, jsonify, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from v1.meetups import models
from v1.auth.models import users

rsvp_m = Blueprint('rsvp', __name__, url_prefix='/api/v1/')


@rsvp_m.route('/meetups/<int:m_id>/rsvps', methods=['POST'])
@jwt_required
def rsvp_meetup(m_id):

    try:
        status = request.json['status']

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

        rsvp = {
            "m_id": m_id,
            "u_id": userid,
            "status": status
        }

        # get the meetup topic using meetup id
        try:
            title = [t for t in models.meetups if t['id'] == m_id][0]['title']
        except IndexError:
            return jsonify(
                {
                    "status": 500,
                    "error": "error retrieving meetup title"
                }), 500

        # check if user has already rsvp'd
        # if they have, update the record
        # if not, append
        if any(u['u_id'] == userid and u['m_id'] == m_id for u in models.rsvps):
            # TODO: HANDLE DUPLICATES HERE. THIS DOES NOT WORK AS EXPECTED
            models.rsvps.append(rsvp)
            return jsonify(
                {
                    "status": 200,
                    "msg": "rsvp updated successfully",
                    "data": [{
                        "m_id": m_id,
                        "status": status,
                        "topic": title
                    }]
                }), 200
        else:
            models.rsvps.append(rsvp)
            return jsonify(
                {
                    "status": 201,
                    "msg": "meetup rsvp successful",
                    "data": [{
                        "m_id": m_id,
                        "status": status,
                        "topic": title
                    }]
                }
            ), 201
    except (ValueError, KeyError, TypeError):
        abort(400)
