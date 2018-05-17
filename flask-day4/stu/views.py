
from flask import Blueprint, render_template, request
from stu.models import db, Student
from sqlalchemy import and_, or_, not_

stu = Blueprint('stu', __name__)


@stu.route('/')
def index():
    return render_template('index.html')


@stu.route('/createdb/')
def create_db():
    db.create_all()
    return '创建数据库成功'


@stu.route('/createstu/', methods=['GET', 'POST'])
def create_stu():
    if request.method == 'GET':
        return render_template('create_stu.html')

    if request.method == 'POST':
        username = request.form.get('username')
        age = request.form.get('age')

        stus = Student(username, age)
        db.session.add(stus)
        db.session.commit()

        return '创建成功'


@stu.route('/createstus', methods=['GET', 'POST'])
def create_stus():
    if request.method == 'GET':
        return render_template('create_stu.html')
    else:
        stus_list = []
        username1 = request.form.get('username1')
        age1 = request.form.get('age1')

        username2 = request.form.get('username2')
        age2 = request.form.get('age2')

        stu1 = Student(username1, age1)
        stu2 = Student(username2, age2)

        stus_list.append(stu1)
        stus_list.append(stu2)

        db.session.add_all(stus_list)
        db.session.commit()
        return '创建成功'


@stu.route('/selectstu/')
def select_stu():
    # 年龄小于16岁的学生的信息
    stus = Student.query.filter(Student.s_age < 16)
    # 小于等于16
    stus = Student.query.filter(Student.s_age.__le__(16))
    # 年龄大于16
    stus = Student.query.filter(Student.s_age.__gt__(16))
    # 年龄大于等于16
    stus = Student.query.filter(Student.s_age.__ge__(16))

    # 年龄在16,1,20,34,23,32
    stus = Student.query.filter(Student.s_age.in_([16, 1, 20, 34, 23, 32]))

    # 获取所有学生信息
    #sql = 'select * from student;'
    #stus = db.session.execute(sql)

    # 按照id降序排列
    stus = Student.query.order_by('-s_id')

    # 按照id降序获取三个
    stus = Student.query.order_by('-s_id').limit(3)

    # 获取年龄最大的一个
    stus = Student.query.order_by('-s_age').first()

    # 跳过3个数据，查询5个信息
    stus = Student.query.order_by('-s_age').offset(3).limit(5)

    # 跳过3个数据
    stus = Student.query.order_by('-s_age').offset(3)

    # 获取id等于24的学生
    stus = Student.query.filter(Student.s_id == 24)
    stus = Student.query.get(24)

    # 查询多个条件
    stus = Student.query.filter(Student.s_age == 18, Student.s_name == '雅典娜')

    # and_ 并且条件
    stus = Student.query.filter(and_(Student.s_age == 18, Student.s_name == '雅典娜'))

    # or_ 或者条件
    stus = Student.query.filter(or_(Student.s_age == 18, Student.s_name == '火神'))

    # not_ 非
    stus = Student.query.filter(not_(Student.s_age == 18), Student.s_name == '火神')

    return render_template('student_list.html', stus=stus)


@stu.route('/stupage/')
def stu_page():

    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    paginate = Student.query.order_by('-s_id').paginate(page, per_page, error_out=False)

    stus = paginate.items
    return render_template('stupage.html', paginate=paginate, stus=stus)


@stu.route('/selectgradebystu/<int:id>/')
def select_grade_by_stu(id):

    stu = Student.query.get(id)
    grade = stu.stu

    return render_template('student_grade.html', grade=grade, stu=stu)
