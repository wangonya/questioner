from flask import jsonify, Blueprint
from api.v1.meetups import models

upcoming_meetups = Blueprint('upcoming_meetups', __name__, url_prefix='/api/v1/')
specific_meetup = Blueprint('specific_meetup', __name__, url_prefix='/api/v1/')


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
