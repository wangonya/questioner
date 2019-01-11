import os
from flask import Flask, Blueprint
from flask_jwt_extended import JWTManager
from flask_restful import Api, Resource

from api.v1.auth.sign_up import sign_up
from api.v1.auth.log_in import log_in
from api.v1.auth.reset import reset
from api.v1.meetups.view_meetups import upcoming_meetups, specific_meetup, admin_meetup
from api.v1.meetups.create_meetup import create_m
from api.v1.meetups.rsvp import rsvp_m
from api.v1.questions.post_questions import post_q
from api.v1.questions.answer_question import answer_q
from api.v1.questions.vote import upvote_q, downvote_q


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    api_bp = Blueprint('api', __name__)
    api = Api(api_bp)
    jwt = JWTManager(app)

    # register blueprint
    app.register_blueprint(api_bp, url_prefix='/api/v1')

    app.config.from_mapping(
        SECRET_KEY='questioner-dev-secret-key',
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
        def get(self):
            return {'hello': 'world'}

    # register routes
    api.add_resource(HelloWorld, '/')

    return app
