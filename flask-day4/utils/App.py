

from flask import Flask
from stu.views import stu
from grade.views import grade
from utils.settings import template_dir, static_dir, SQLACHEMY_DATABASE_URI
from utils.functions import init_ext


def create_app():

    app = Flask(__name__, template_folder=template_dir,
                static_folder=static_dir)

    app.debug = True
    app.register_blueprint(blueprint=stu, url_prefix='/stu')
    app.register_blueprint(blueprint=grade, url_prefix='/grade')

    app.config['SQLALCHEMY_DATABASE_URI'] = SQLACHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = '<replace with a secret key>'

    init_ext(app)

    return app
