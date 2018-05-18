

from datetime import datetime
from utils.functions import db


class Grade(db.Model):

    g_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    g_name = db.Column(db.String(10), unique=True)
    g_desc = db.Column(db.String(100), nullable=True)
    g_time = db.Column(db.Date, default=datetime.now)
    # backref='stu' 是通过stu来找班级，即student.stu
    students = db.relationship('Student', backref='stu', lazy=True)

    __tablename__ = 'grade'

    def __init__(self, name, desc):

        self.g_name = name
        self.g_desc = desc


