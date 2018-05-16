import random
from flask import Blueprint, render_template, redirect, url_for
from Stu.models import db, Student

stu = Blueprint('stu', __name__)


@stu.route('/')
def index():

    return render_template('index.html')


@stu.route('/scores/')
def scores():

    scores_list = [21, 34, 32, 67, 88, 98, 67, 45]
    content_h2 = '<h2>今天你真帅</h2>'
    content_h3 = ' <h3>我真帅</h3> '
    return render_template('scores.html', scores=scores_list, content=content_h2, content1=content_h3)


@stu.route('/createtable/')
def create_db():
    db.create_all()
    return '创建成功'


# 删除数据库
@stu.route('/droptable/')
def drop_db():
    db.drop_all()
    return '删除成功'


@stu.route('/createstu/')
def create_stu():
    stu = Student()
    stu.s_name = '李白%d' % random.randrange(1000)
    stu.s_age = '%d' % random.randrange(20)

    db.session.add(stu)
    try:
        db.session.commit()

    except:
        db.session.rollback()

    return '创建学生成功'


@stu.route('/stulist/')
def stu_all():

    stus = Student.query.all()
    # sql = 'select*from student;'
    # stus = db.session.execute(sql)
    # 使用filter
    # stus = Student.query.filter(Student.s_name == '李白515')
    # 使用filter_by
    # stus = Student.query.filter_by(s_name='李白515')

    return render_template('stulist.html', stus=stus)


@stu.route('/update/')
def update_stu():

    # stu = Student.query.filter_by(s_id=5).first()
    # stu.s_name = '李二狗'

    # 第二种方式
    Student.query.filter(Student.s_id == 5).update({'s_name': '李二狗'})

    db.session.commit()

    return redirect(url_for('stu.stu_all'))


@stu.route('/deletestu/')
def delete_stu():

    stu = Student.query.filter(Student.s_id==5).first()

    db.session.delete(stu)
    db.session.commit()

    return redirect(url_for('stu.stu_all'))
