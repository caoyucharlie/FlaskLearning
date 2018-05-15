
import random
from flask import Blueprint, render_template, request, session, redirect,\
    url_for, make_response


blue = Blueprint('app', __name__)


@blue.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        username = session.get('username')
        return render_template('login.html', username=username)
    else:
        username = request.form.get('username')
        session['username'] = username

        return redirect(url_for('app.login'))


@blue.route('/getresponse/')
def get_response():

    response = make_response('<h2>fuck off</h2>', 200)
    ticket = ''
    s = 'qwertyuiopasdfghjklzxcvbnm1234567890'
    for i in range(20):
        ticket += random.choice(s)
    response.set_cookie('ticket', ticket)
    return response


@blue.route('/deletecookie')
def del_cookie():
    response = make_response('<h2>shit</h2>', 200)
    response.delete_cookie('ticket')

    return response
