

from utils.functions import db


class Student(db.Model):
    s_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(20), unique=True)
    s_age = db.Column(db.Integer, default=18)
    s_g = db.Column(db.Integer, db.ForeignKey('grade.g_id'), nullable=True)

    __tablename__ = 'stu'

    def __init__(self, name, age):
        self.s_name = name
        self.s_age = age


sc = db.Table('sc',       # 中间表名
              db.Column('s_id', db.Integer, db.ForeignKey('stu.s_id'), primary_key=True),
              db.Column('c_id', db.Integer, db.ForeignKey('course.c_id'), primary_key=True)
              )


class Course(db.Model):

    c_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    c_name = db.Column(db.String(10), unique=True)
    students = db.relationship('Student',
                               secondary=sc,     # 指定代理
                               backref='cou'     # 通过 cou反向查找
                               )

    __tablename__ = 'course'

    def __init__(self, name):
        self.c_name = name



