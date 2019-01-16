from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity

from ..meetups.models import MeetupModel
from ..auth.models import AuthModel
from api.v1.utils.validators import MeetupValidators
from api.v1.utils.error_handlers import AdminProtectedError


class Meetups(Resource):
    """upcoming meetups endpoint resource"""
    parser = reqparse.RequestParser()
    parser.add_argument("title",
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")
    parser.add_argument("location",
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")
    parser.add_argument("happening_on",
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")
    parser.add_argument("image",
                        type=str)
    parser.add_argument("tags", action="append")

    @staticmethod
    def get():
        """do a GET to upcoming meetups endpoint"""
        return {"status": 200,
                "data": MeetupModel.meetups}, 200


class PostMeetups(Resource):
    """post new meetup endpoint"""
    @jwt_required
    def post(self):
        """do a POST to the meetups endpoint"""
        data = Meetups.parser.parse_args()

        # get current user from jwt token
        user = get_jwt_identity()
        creator = AuthModel.find_by_uid(user)
        is_admin = AuthModel.check_if_admin(user)

        if creator and is_admin:
            title = data["title"]
            creator_id = creator
            location = data["location"]
            happening_on = data["happening_on"]
            tags = data["tags"]
            image = data["image"]

            # handle duplicates
            MeetupValidators.check_duplicate_meetup(title, creator_id)

            meetup = MeetupModel(title, creator_id, location,
                                 happening_on, tags, image)
            meetup.save_meetup_to_db()

            response = {
                "status": 200,
                "message": "meetup created successfully",
                "data": [{
                    "title": title,
                    "location": location,
                    "happeningOn": happening_on,
                    "tags": tags,
                }]}

            return response, 201
        else:
            raise AdminProtectedError


class GetSpecificMeetup(Resource):
    @staticmethod
    def get(m_id):
        meetup = MeetupModel.find_by_m_id(m_id)

        response = {
            "status": 200,
            "data": [meetup]
                }

        return response, 200


class GetAdminMeetups(Resource):
    @jwt_required
    def get(self, uid):
        user = get_jwt_identity()
        is_admin = AuthModel.check_if_admin(user)

        if is_admin:
            meetups = MeetupModel.find_admin_meetups(uid)

            response = {
                "status": 200,
                "data": meetups
            }

            return response, 200
