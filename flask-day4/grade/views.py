
from flask import Blueprint, render_template
from grade.models import db, Grade

grade = Blueprint('grade', __name__)


@grade.route('/')
def get_grade():

    return '我是班级'


@grade.route('/createdb/')
def create_db():
    db.create_all()
    return '创建数据库成功'


@grade.route('/creategrade/')
def add_grade():
    names = {
        'python': '人生苦短,我用python',
        'h5': '我是前端',
        'java': '佳娃',
        'go': 'gogogogo'
    }
    grades_list = []
    for key in names.keys():
        grade = Grade(key, names[key])
        grades_list.append(grade)

    db.session.add_all(grades_list)
    db.session.commit()

    return '创建成功'


@grade.route('/selectstubygrade/<int:id>/')
def select_stu_by_grade(id):
    grade = Grade.query.get(id)
    stus = grade.students

    return render_template('grade_student.html',
                           stus=stus,
                           grade=grade)


