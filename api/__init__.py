import os

from flask import Flask, Blueprint
from flask_jwt_extended import JWTManager
from flask_restful import Api, Resource

from .error_handlers import errors

from .v1.auth.sign_up import Signup
from .v1.auth.log_in import Login
from .v1.auth.reset import Reset
from .v1.meetups.meetups import Meetups, GetSpecificMeetup, GetAdminMeetups
from .v1.meetups.rsvp import Rsvp
from .v1.questions.post_questions import PostQuestion
from .v1.questions.answer_question import AnswerQuestion
from .v1.questions.vote import Upvote, DownVote


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    api_bp = Blueprint('api', __name__)
    api = Api(api_bp, errors=errors)
    jwt = JWTManager(app)

    # register blueprint
    app.register_blueprint(api_bp, url_prefix='/api/v1')

    app.config.from_mapping(
        SECRET_KEY='questioner-dev-secret-key',
        JWT_SECRET_KEY='questioner-jwt-secret-key',
        PROPAGATE_EXCEPTIONS=True
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.cfg', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    class HelloWorld(Resource):
        @staticmethod
        def get():
            return {'hello': 'world'}

    # register routes
    api.add_resource(HelloWorld, '/')
    api.add_resource(Signup, '/auth/signup')
    api.add_resource(Login, '/auth/login')
    api.add_resource(Reset, '/auth/reset')
    api.add_resource(Meetups, '/meetups/upcoming')
    api.add_resource(GetSpecificMeetup, '/meetups/<int:m_id>')
    api.add_resource(GetAdminMeetups, '/admin/profile/<int:uid>')
    api.add_resource(Rsvp, '/meetups/<int:m_id>/rsvps')
    api.add_resource(PostQuestion, '/questions')
    api.add_resource(AnswerQuestion, '/questions/<int:q_id>/answer')
    api.add_resource(Upvote, '/questions/<int:q_id>/upvote')
    api.add_resource(DownVote, '/questions/<int:q_id>/downvote')

    return app
