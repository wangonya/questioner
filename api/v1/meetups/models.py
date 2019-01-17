from datetime import datetime

from api.v1.utils.error_handlers import DataIndexError, DuplicateDataError


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
    def return_all_meetups(cls):
        meetups = [meetup.__dict__ for meetup in cls.meetups]
        return meetups

    @classmethod
    def find_by_m_id(cls, m_id):
        """find required meetup from db using its id"""
        try:
            meetup = [meetup for meetup in cls.meetups if meetup.m_id == m_id][0]
        except IndexError:
            raise DataIndexError
        return vars(meetup)

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
            meetup = [meetup.__dict__ for meetup in cls.meetups if meetup.creator == uid][0]
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

    @classmethod
    def check_duplicate_rsvp(cls, userid, m_id):
        """check if user has already rsvp'd
        if they have, remove the record"""
        if any(r.uid == userid and r.m_id == m_id for r in cls.rsvps):
            rsvp_index = [i for i, r in enumerate(cls.rsvps) if r.uid == userid and r.m_id == m_id][0]
            cls.rsvps.pop(rsvp_index)
