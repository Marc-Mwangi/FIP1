from flask import render_template
from app import app

#Views
@app.route('/')
def dashboard():

    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def sigup():
    return render_template('signup.html')