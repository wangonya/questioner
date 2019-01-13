from datetime import datetime

from ...error_handlers import DataIndexError


class MeetupModel:
    meetups = [
        {
            "id": 1,
            "title": "sample meetup",
            "location": "test location",
            "happeningOn": "test date",
            "tags": ["tag1", "tag2", "tag3"],
            "creator": 1
        },
        {
            "id": 2,
            "title": "sample meetup2",
            "location": "test location2",
            "happeningOn": "test date2",
            "tags": ["tag1", "tag2", "tag3"],
            "creator": 1
        }
    ]

    rsvps = []

    def __init__(self, title, creator, location,
                 happening_on, tags, image):
        self.m_id = len(MeetupModel.meetups) + 1
        self.title = title
        self.creator = creator
        self.location = location
        self.happening_on = happening_on
        self.created_on = datetime.now()
        self.tags = tags,
        self.image = image

    def save_meetup_to_db(self):
        MeetupModel.meetups.append(self)

    def save_rsvp_to_db(self):
        MeetupModel.rsvps.append(self)

    @classmethod
    def find_by_m_id(cls, m_id):
        try:
            meetup = [meetup for meetup in cls.meetups if meetup["id"] == m_id][0]
        except IndexError:
            raise DataIndexError
        return meetup

    @classmethod
    def find_admin_meetups(cls, uid):
        try:
            meetup = [meetup for meetup in cls.meetups if meetup["creator"] == uid]
        except IndexError:
            raise DataIndexError
        return meetup
