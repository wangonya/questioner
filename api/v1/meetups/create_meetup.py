from flask import request, abort, jsonify, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
import datetime as date
from v1.meetups import models
from v1.auth.models import users

create_m = Blueprint('create_m', __name__, url_prefix='/api/v1/')


# TODO: CHECK TO ENSURE USER IS ADMIN BEFORE POSTING
@create_m.route('/meetups', methods=['POST'])
@jwt_required
def create_meetup():

    try:
        title = request.json['title']
        location = request.json['location']
        happening_on = request.json['happeningOn']
        tags = request.json['tags']
        images = request.json['image']

        try:
            m_id = models.meetups[-1]['id'] + 1
        except IndexError:
            m_id = 1

        # get current user from jwt token
        user = get_jwt_identity()

        # get a list of the user object with the matching email retrieved from get_jwt_identity()
        # and retrieve the user id from it
        try:
            userid = [u for u in users if u['email'] == user][0]['id']
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

        meetup = {
            "id": m_id,
            "title": title,
            "createdBy": userid,
            "location": location,
            "happeningOn": happening_on,
            "createdOn": date.datetime.now(),
            "tags": tags,
            "images": images
        }
        models.meetups.append(meetup)
        return jsonify(
            {
                "status": 201,
                "msg": "meetup added successfully",
                "data": [{
                    "id": m_id,
                    "title": title,
                    "createdBy": userid,
                    "location": location,
                    "happeningOn": happening_on,
                    "createdOn": date.datetime.now(),
                    "tags": tags,
                    "images": images
                }]
            }
        ), 201
    except (ValueError, KeyError, TypeError):
        abort(400)
