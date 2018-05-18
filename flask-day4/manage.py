
from flask_script import Manager
from utils.App import create_app

app = create_app()
manger = Manager(app=app)


if __name__ == '__main__':
    app.run()
