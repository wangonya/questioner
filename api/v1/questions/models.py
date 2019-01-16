from datetime import datetime

from ...error_handlers import DataIndexError


class PostQuestionsModel:
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
        PostQuestionsModel.questions.append(self)

    @classmethod
    def find_by_q_id(cls, q_id):
        try:
            question = [question for question in cls.questions if question.q_id == q_id][0]
        except IndexError:
            raise DataIndexError
        return question

    @classmethod
    def find_meetup_by_q_id(cls, q_id):
        try:
            meetup = [q.meetup for q in cls.questions if q.q_id == q_id][0]
        except IndexError:
            raise DataIndexError
        return meetup

    @classmethod
    def find_title_by_q_id(cls, q_id):
        try:
            title = [q.title for q in cls.questions if q.q_id == q_id][0]
        except IndexError:
            raise DataIndexError
        return title

    @classmethod
    def find_body_by_q_id(cls, q_id):
        try:
            body = [q.body for q in cls.questions if q.q_id == q_id][0]
        except IndexError:
            raise DataIndexError
        return body


class AnswerQuestionsModel:
    answers = []

    def __init__(self, body, creator, meetup, for_question):
        self.a_id = len(AnswerQuestionsModel.answers) + 1
        self.body = body
        self.creator = creator
        self.meetup = meetup
        self.for_question: for_question

    def save_answer_to_db(self):
        AnswerQuestionsModel.answers.append(self)


class VoteModel:
    votes = []

    @classmethod
    def save_upvote_to_db(cls, voter, question):
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

