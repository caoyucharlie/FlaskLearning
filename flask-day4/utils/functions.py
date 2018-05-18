from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_restful import Api
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
debugtoolbar = DebugToolbarExtension()
api = Api()
ma = Marshmallow()


def get_db_uri(DATABASE):

    user = DATABASE.get('USER')
    password = DATABASE.get('PASSWORD')
    host = DATABASE.get('HOST')
    port = DATABASE.get('PORT')
    name = DATABASE.get('NAME')
    db = DATABASE.get('DB')
    driver = DATABASE.get('DRIVER')

    return '{}+{}://{}:{}@{}:{}/{}'.format(db, driver,
                                           user, password,
                                           host, port, name)


def init_ext(app):

    db.init_app(app=app)
    debugtoolbar.init_app(app=app)
    api.init_app(app=app)
    ma.init_app(app=app)
