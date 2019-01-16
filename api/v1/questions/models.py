from datetime import datetime

from api.v1.utils.error_handlers import DataIndexError


class PostQuestionsModel:
    """model to handle questions data"""
    questions = []
    
    def __init__(self, title, creator, body, meetup):
        self.q_id = len(PostQuestionsModel.questions) + 1
        self.title = title
        self.creator = creator
        self.body = body
        self.meetup = meetup
        self.created_on = datetime.now()
        self.votes = 0

    def save_question_to_db(self):
        """save entered question data to db"""
        PostQuestionsModel.questions.append(self)

    @classmethod
    def find_by_q_id(cls, q_id):
        """find required question from db using its id"""
        try:
            question = [question for question in cls.questions if question.q_id == q_id][0]
        except IndexError:
            raise DataIndexError
        return question

    @classmethod
    def find_meetup_by_q_id(cls, q_id):
        """find required meetup from db using the question id"""
        try:
            meetup = [q.meetup for q in cls.questions if q.q_id == q_id][0]
        except IndexError:
            raise DataIndexError
        return meetup

    @classmethod
    def find_title_by_q_id(cls, q_id):
        """find required question title from db using its id"""
        try:
            title = [q.title for q in cls.questions if q.q_id == q_id][0]
        except IndexError:
            raise DataIndexError
        return title

    @classmethod
    def find_body_by_q_id(cls, q_id):
        """find required question body from db using its id"""
        try:
            body = [q.body for q in cls.questions if q.q_id == q_id][0]
        except IndexError:
            raise DataIndexError
        return body

    @classmethod
    def find_duplicate_question(cls, title, meetup):
        """check if a similar question exists in the meetup"""
        return any(q for q in cls.questions if q.title == title and q.meetup == meetup)


class AnswerQuestionsModel:
    """model to handle answers data"""
    answers = []

    def __init__(self, body, creator, meetup, question):
        self.a_id = len(AnswerQuestionsModel.answers) + 1
        self.body = body
        self.creator = creator
        self.meetup = meetup
        self.question = question

    def save_answer_to_db(self):
        """save entered answer to db"""
        AnswerQuestionsModel.answers.append(self)

    @classmethod
    def find_duplicate_answer(cls, body, question):
        """check if a similar answer exists in the question"""
        return any(a for a in cls.answers if a.body == body and a.question == question)


class VoteModel:
    """model to handle votes data"""
    votes = []

    @classmethod
    def save_upvote_to_db(cls, voter, question):
        """save entered vote to db"""
        upvote = {
            "user": voter,
            "question": question,
            "count": 1
        }

        downvote = {
            "user": voter,
            "question": question,
            "count": -1
        }

        # check if user has already voted
        # if they have, remove the record
        # if not, append
        if any(v["user"] == voter and v["question"] == question for v in cls.votes):
            try:
                cls.votes.remove(upvote)
            except ValueError:  # the vote was a downvote, so remove that instead
                cls.votes.remove(downvote)
        else:
            cls.votes.append(upvote)

        return sum(s["count"] for s in cls.votes)

    @classmethod
    def save_downvote_to_db(cls, voter, question):
        """save entered vote to db"""
        upvote = {
            "user": voter,
            "question": question,
            "count": 1
        }

        downvote = {
            "user": voter,
            "question": question,
            "count": -1
        }

        # check if user has already voted
        # if they have, remove the record
        # if not, append
        if any(v["user"] == voter and v["question"] == question for v in cls.votes):
            try:
                cls.votes.remove(downvote)
            except ValueError:  # the vote was a upvote, so remove that instead
                cls.votes.remove(upvote)
        else:
            cls.votes.append(downvote)

        return sum(s["count"] for s in cls.votes)

