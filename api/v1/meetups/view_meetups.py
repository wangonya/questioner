from flask import jsonify, Blueprint
from v1.meetups import models

upcoming_meetups = Blueprint('upcoming_meetups', __name__, url_prefix='/api/v1/')


@upcoming_meetups.route('/meetups/upcoming', methods=['GET'])
def get_upcoming_meetups():
    return jsonify(
        {
            "status": 200,
            "data": models.meetups
        }), 200
