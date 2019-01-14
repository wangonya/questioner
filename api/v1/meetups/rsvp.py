from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..meetups.models import MeetupModel, RsvpsModel
from ..auth.models import AuthModel


class Rsvp(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("status",
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")

    # TODO: CHECK FOR AND HANDLE DUPLICATES
    @jwt_required
    def post(self, m_id):
        data = Rsvp.parser.parse_args()
        status = data["status"]
        user = get_jwt_identity()
        userid = AuthModel.find_by_uid(user)
        title = MeetupModel.find_by_m_id(m_id)

        rsvp = RsvpsModel(status, userid, m_id)
        rsvp.save_rsvp_to_db()

        response = {
            "status": 201,
            "msg": "meetup rsvp successful",
            "data": [{
                "m_id": m_id,
                "status": status,
                "topic": title["title"]
                }]
            }

        return response, 201
