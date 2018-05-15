import os
from flask import Flask
from App.views import blue


def create_app():

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    static_dir = os.path.join(BASE_DIR, 'static')

    templates_dir = os.path.join(BASE_DIR, 'templates')

    app = Flask(__name__, static_folder=static_dir,
                template_folder=templates_dir)
    app.register_blueprint(blueprint=blue, url_prefix='/hello')

    return app
