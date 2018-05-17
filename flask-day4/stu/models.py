
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    s_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(20), unique=True)
    s_age = db.Column(db.Integer, default=18)
    s_g = db.Column(db.Integer, db.ForeignKey('grade.g_id'), nullable=True)

    __tablename__ = 'stu'

    def __init__(self, name, age):
        self.s_name = name
        self.s_age = age

