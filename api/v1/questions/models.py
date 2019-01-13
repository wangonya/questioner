from datetime import datetime

from ...error_handlers import DataIndexError


class PostQuestionsModel:
    questions = [
        {
          "body": "test body.",
          "q_id": 1,
          "meetup": 1,
          "title": "test"
        }
    ]
    
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
            question = [question for question in cls.questions if question["q_id"] == q_id][0]
        except IndexError:
            raise DataIndexError
        return question

    @classmethod
    def find_meetup_by_q_id(cls, q_id):
        try:
            meetup = [q["meetup"] for q in cls.questions if q["q_id"] == q_id][0]
        except IndexError:
            raise DataIndexError
        return meetup


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
    pass
