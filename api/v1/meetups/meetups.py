from flask import jsonify, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from api.v1.meetups import models
from api.v1.auth.models import users

upcoming_meetups = Blueprint('upcoming_meetups', __name__, url_prefix='/api/v1/')
specific_meetup = Blueprint('specific_meetup', __name__, url_prefix='/api/v1/')
admin_meetup = Blueprint('admin_meetup', __name__, url_prefix='/api/v1/')


@upcoming_meetups.route('/meetups/upcoming', methods=['GET'])
def get_upcoming_meetups():
    return jsonify(
        {
            "status": 200,
            "data": models.meetups
        }), 200


@specific_meetup.route('/meetups/<int:m_id>', methods=['GET'])
def get_specific_meetup(m_id):
    meetup = [meetup for meetup in models.meetups if meetup['id'] == m_id]
    if len(meetup) == 0:
        return jsonify(
            {
                "status": 404,
                "error": "a meetup with id {} does not exist".format(m_id)
            }), 404
    else:
        return jsonify(
            {
                "status": 200,
                "data": meetup[0]
            }), 200


@admin_meetup.route('/admin/profile/<int:u_id>', methods=['GET'])
@jwt_required
def get_admin_meetup(u_id):

    # get current user from jwt token
    user = get_jwt_identity()

    # check if that user exists
    # and if the user is admin
    try:
        is_admin = [u for u in users if u['email'] == user][0]['isAdmin']
        if not is_admin:
            return jsonify(
                    {
                        "status": 401,
                        "error": "only admin can post meetups"
                    }), 401
    except IndexError:
        return jsonify(
                {
                    "status": 500,
                    "error": "error retrieving user"
                }), 500
    meetup = [meetup for meetup in models.meetups if meetup['createdBy'] == u_id]
    return jsonify(
            {
                "status": 200,
                "data": meetup
            }), 200
        
