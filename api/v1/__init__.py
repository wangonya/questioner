from flask import Flask
from v1.auth.sign_up import sign_up


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.cfg')

    @app.route('/')
    def hello():
        return "Hello World!"

    # register blueprints
    app.register_blueprint(sign_up)

    return app
