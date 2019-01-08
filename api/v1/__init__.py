from flask import Flask
from v1.auth.sign_up import sign_up
from v1.auth.log_in import log_in
from v1.auth.reset import reset


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.cfg')

    @app.route('/')
    def hello():
        return "Hello World!"

    # register blueprints
    app.register_blueprint(sign_up)
    app.register_blueprint(log_in)
    app.register_blueprint(reset)

    return app
