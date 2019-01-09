import os
from flask import Flask
from flask_jwt_extended import JWTManager
from v1.auth.sign_up import sign_up
from v1.auth.log_in import log_in
from v1.auth.reset import reset
from v1.meetups.view_meetups import upcoming_meetups, specific_meetup
from v1.meetups.create_meetup import create_m
from v1.questions.post_questions import post_q
from v1.questions.vote import upvote_q


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    jwt = JWTManager(app)

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

    @app.route('/')
    def hello():
        return "Hello World!"

    # register blueprints
    app.register_blueprint(sign_up)
    app.register_blueprint(log_in)
    app.register_blueprint(reset)
    app.register_blueprint(upcoming_meetups)
    app.register_blueprint(specific_meetup)
    app.register_blueprint(post_q)
    app.register_blueprint(upvote_q)
    app.register_blueprint(create_m)

    return app
