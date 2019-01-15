from datetime import datetime

from ...error_handlers import DataIndexError


class MeetupModel:
    meetups = []

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

    @classmethod
    def find_by_m_id(cls, m_id):
        try:
            meetup = [meetup for meetup in cls.meetups if meetup.m_id == m_id][0]
        except IndexError:
            raise DataIndexError
        return meetup

    @classmethod
    def find_title_by_m_id(cls, m_id):
        try:
            meetup = [meetup.title for meetup in cls.meetups if meetup.m_id == m_id][0]
        except IndexError:
            raise DataIndexError
        return meetup

    @classmethod
    def find_admin_meetups(cls, uid):
        try:
            meetup = [meetup for meetup in cls.meetups if meetup.creator == uid]
        except IndexError:
            raise DataIndexError
        return meetup


class RsvpsModel:
    rsvps = []

    def __init__(self, status, uid, m_id):
        self.rsvp_id = len(RsvpsModel.rsvps) + 1
        self.status = status
        self.uid = uid
        self.m_id = m_id

    def save_rsvp_to_db(self):
        RsvpsModel.rsvps.append(self)
