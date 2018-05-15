
import os
from flask import Flask
from flask_session import Session
import redis
from App.views import blue


def create_app():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    templates_dir = os.path.join(BASE_DIR, 'templates')
    static_dir = os.path.join(BASE_DIR, 'static')

    app = Flask(__name__, template_folder=templates_dir, static_folder=static_dir)

    app.register_blueprint(blueprint=blue, url_prefix='/app')
    # 密钥
    app.config['SECRET_KEY'] = 'secret_key'
    # 使用redis存储信息， 默认访问redis了，127.0.0.1:6379
    app.config['SESSION_TYPE'] = 'redis'
    # 连阿里云的redis
    app.config['SESSION_REDIS'] = redis.Redis(host='47.106.144.34', port='6379', password='jy2190883')
    # 第一种初始化app
    Session(app)
    # 第二种初始化app
    # se = Session()
    # se.init_app(app)
    # 定义前缀
    app.config['SESSION_KEY_PREFIX'] = 'flask'

    return app
