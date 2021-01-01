import os

from flask import Flask
from . import display


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return 'Hello, World!'

    app.register_blueprint(display.bp)

    return app
