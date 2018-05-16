import os
from flask import Flask
from Stu.views import stu
from flask_sqlalchemy import SQLAlchemy


def creat_app():

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    static_dir = os.path.join(BASE_DIR, 'static')
    templates_dir = os.path.join(BASE_DIR, 'templates')

    app = Flask(__name__, template_folder=templates_dir,
                static_folder=static_dir)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:jy2190883@47.106.144.34:3306/flask3'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.register_blueprint(blueprint=stu, url_prefix='/stu')

    SQLAlchemy(app=app)

    return app
