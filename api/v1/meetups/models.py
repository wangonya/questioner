from datetime import datetime

from api.v1.utils.error_handlers import DataIndexError


class MeetupModel:
    """model to handle meetup data"""
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
        """save entered meetup data to db"""
        MeetupModel.meetups.append(self)

    @classmethod
    def find_by_m_id(cls, m_id):
        """find required meetup from db using its id"""
        try:
            meetup = [meetup for meetup in cls.meetups if meetup.m_id == m_id][0]
        except IndexError:
            raise DataIndexError
        return meetup

    @classmethod
    def find_title_by_m_id(cls, m_id):
        """find required meetup title from db using its id"""
        try:
            meetup = [meetup.title for meetup in cls.meetups if meetup.m_id == m_id][0]
        except IndexError:
            raise DataIndexError
        return meetup

    @classmethod
    def find_admin_meetups(cls, uid):
        """find meetups created by a particular admin from db using the admin's id"""
        try:
            meetup = [meetup for meetup in cls.meetups if meetup.creator == uid]
        except IndexError:
            raise DataIndexError
        return meetup

    @classmethod
    def find_duplicate_meetup(cls, title, creator):
        """check if the same creator has entered a meetup with the same title"""
        return any(m for m in cls.meetups if m.title == title and m.creator == creator)


class RsvpsModel:
    """model to handle rsvp data"""
    rsvps = []

    def __init__(self, status, uid, m_id):
        self.rsvp_id = len(RsvpsModel.rsvps) + 1
        self.status = status
        self.uid = uid
        self.m_id = m_id

    def save_rsvp_to_db(self):
        """save entered rsvp data to db"""
        RsvpsModel.rsvps.append(self)
