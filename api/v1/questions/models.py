from datetime import datetime


class PostQuestionsModel:
    questions = [
        {
          "body": "test body.",
          "id": 1,
          "meetup": 1,
          "title": "test"
        }
    ]
    
    def __init__(self, title, creator, body, meetup):
        self.m_id = len(PostQuestionsModel.questions) + 1
        self.title = title
        self.creator = creator
        self.body = body
        self.meetup = meetup
        self.created_on = datetime.now()
        self.votes = 0

    def save_question_to_db(self):
        PostQuestionsModel.questions.append(self)


class AnswerQuestionsModel:
    pass


class VoteModel:
    pass
