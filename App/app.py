import os
from flask import Flask, url_for,render_template, request, flash, redirect, session
#import the user object
from app import User_obj

#create the flask app
app = Flask(__name__, template_folder='../templates', static_folder='../assets')
app.config.from_object(__name__)
app.config.update(dict(
    SECRET_KEY='topsecretkey',
    #this should be set to false in production
    DEBUG=True
))
@app.route('/')
def index():
    """route to render home page"""
    return render_template('index.html')

@app.route('/login')
def login():
    """route to render login page"""
    return render_template('login.html')

@app.route('/dashboard')
def dashboard_view():
    """route to render dashboard page"""
    return render_template('dashboard.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    confpassword = request.form['confpassword']

    if password != confpassword:
        flash('passwords do not match', 'alert-danger')
        return redirect(url_for('signup'))
    res = User_obj.signup(username, email, password)
    if res == "username or email exists":
        flash('username or email already taken', 'alert-danger')
        return redirect(url_for('signup'))
    flash('signup successful. now login', 'alert-success')
    return redirect(url_for('login'))

@app.route ('/session', methods =['POST'])
def session ():
    username = request.form['username']
    password = request.form['password']
    res = User_obj.login(username=username, password=password)
    print(res)
    if res == True:
        return redirect(url_for('dashboard_view'))
    else:
        flash('wrong username or password', 'alert-danger')
        return redirect(url_for('login'))
