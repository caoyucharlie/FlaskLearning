
from flask import Blueprint, render_template, request, redirect, url_for
from stu.models import db, Student, Course
from sqlalchemy import and_, or_, not_
from flask_restful import Resource
from utils.functions import api
from stu.stumarshmallow import stumarsh

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
    stus = Student.query.filter(or_(Student.s_age == 18, Student.s_name == '李白'))

    # not_ 非
    stus = Student.query.filter(not_(Student.s_age == 18), Student.s_name == '王昭君')

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


@stu.route('/addcourse/')
def add_course():

    courses = ['高数', '大学物理', '线性代数', 'ARM单片机', 'VHDL', '大学英语']
    course_list = []

    for course in courses:
        cou = Course(course)
        course_list.append(cou)

    db.session.add_all(course_list)
    db.session.commit()

    return '添加课程成功'


@stu.route('/stucourse/', methods=['GET', 'POST'])
def stu_cou():
    if request.method == 'GET':
        stus = Student.query.all()
        cous = Course.query.all()
        return render_template('stu_cou.html', stus=stus, cous=cous)

    else:
        s_id = request.form.get('student')
        c_id = request.form.get('course')

        # 第一种方式
        # sql = 'insert into sc(s_id, c_id) values(%s, %s)' %(s_id, c_id)
        #
        # db.session.execute(sql)
        # db.session.commit()
        #
        # return '插入成功'

        # 第二种方式
        stu = Student.query.get(s_id)
        cou = Course.query.get(c_id)

        cou.students.append(stu)
        db.session.add(cou)
        db.session.commit()

        return '插入成功'
        # 第三种(批量插入)
        # s_id = request.form.get('student')
        # c_ids = request.form.getlist('course')
        # stu = Student.query.get(s_id)
        #
        # for c in c_ids:
        #     cou = Course.query.get(c)
        #     cou.students.append(stu)
        #     db.session.add(cou)
        #
        # db.session.commit()
        # return '插入成功'


@stu.route('/allstu/')
def all_stu():
    stus = Student.query.all()

    return render_template('all_stu.html', stus=stus)


@stu.route('/selectcoursebystu/<int:id>/')
def select_course_by_stu(id):
    stu = Student.query.get(id)
    cous = stu.cou
    return render_template('stucourse.html', cous=cous, stu=stu)


@stu.route('/deletecoursebyid/<int:s_id>/<int:c_id>/')
def delete_course_by_id(s_id, c_id):
    stu = Student.query.get(s_id)
    cou = Course.query.get(c_id)

    cou.students.remove(stu)
    db.session.commit()

    return redirect(url_for('stu.all_stu'))


class HelloStudent(Resource):

    def get(self, id):

        stu = Student.query.get(id)
        # data = {'name': stu.s_name,
        #         'age': stu.s_age
        #         }

        return stumarsh.jsonify(stu)

    def post(self, s_id, c_id):
        pass


api.add_resource(HelloStudent, '/api/stu/<int:id>/')
