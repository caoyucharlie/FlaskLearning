from flask import Flask
from flask_script import Manager
from App import create_app

# 初始化， __name__代表主模块名或者包
# app = Flask(__name__)
app = create_app()

manager = Manager(app=app)


if __name__ == '__main__':
    # 启动项目
    # app.run(debug=True, port='8000', host='0.0.0.0')
    manager.run()

