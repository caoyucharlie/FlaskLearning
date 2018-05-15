
from flask import render_template, send_file, request, make_response, redirect, url_for, abort
# from manage import app

from flask import Blueprint
import uuid


blue = Blueprint('first', __name__)

# views.py 主要用于处理业务逻辑


# 路由(127.0.0.1::5000)
@blue.route('/')
def hello_world():
    # 视图函数
    return 'Hello World!'


@blue.route('/hello/<name>/')
def hello_man(name):
    return 'hello name:%s' % name


@blue.route('/helloint/<int:id>')
def hello_int(id):
    return 'Hello int: %s' % (id)


@blue.route('/index/')
def index():
    # return send_file('../templates/hello.html')
    return render_template('hello.html')


@blue.route('/getfloat/<float:price>/')
def hello_float(price):
    return 'float: %s' % price


@blue.route('/getstr/<string:name>/')
def hello_name(name):
    return 'hello name: %s' % name


@blue.route('/getpath/<path:url_path>/')
def hello_path(url_path):
    return 'path: %s' % url_path


@blue.route('/getuuid/')
def hello_get_uuid():
    a = uuid.uuid4()
    return str(a)


@blue.route('/getbyuuid/<uuid:uu>/')
def hello_uuid(uu):
    return 'uu:%s' % uu


@blue.route('/getrequest/', methods=['GET', 'POST'])
def get_request():
    if request.method == 'GET':
        args = request.args
    else:
        form = request.form
    return '获取request'


@blue.route('/makeresponse/')
def make_responses():

    temp = render_template('hello.html')
    # response = make_response('<h2>么么哒</h2>')
    response = make_response(temp)
    return response


@blue.route('/redirect/')
def make_redirect():
    # 第一种方法
    # return redirect('/hello/index/')
    # 第二种方法
    return redirect(url_for('first.index'))


@blue.route('/makeabort/')
def make_abort():
    abort(400)
    return '终结'


@blue.errorhandler(404)
def get_error(exception):

    return '捕捉异常%s' % exception

