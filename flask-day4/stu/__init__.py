import os
from flask import Flask
from stu.views import stu
from flask_sqlalchemy import SQLAlchemy
from grade.views import grade


def create_app():

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_dir = os.path.join(BASE_DIR, 'templates')
    static_dir = os.path.join(BASE_DIR, 'static')

    app = Flask(__name__, template_folder=template_dir,
                static_folder=static_dir)
    app.register_blueprint(blueprint=stu, url_prefix='/stu')
    app.register_blueprint(blueprint=grade, url_prefix='/grade')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:jy2190883@47.106.144.34:3306/flask3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    SQLAlchemy(app=app)

    return app
