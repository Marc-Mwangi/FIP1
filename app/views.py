from flask import redirect, render_template, url_for
from app import app
from .models import User 
from .forms import SignUpForm




app.config['SECRET_KEY'] = 'aSKh3r'

#Views
@app.route('/')
def dashboard():

    title = 'Home - Welcome to The best Movie Review Website Online'

    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def sigup():
    form = SignUpForm()
    if form.validate_on_submit():
        f_name= form.first_name.data
        l_name = form.last_name.data
        password= form.password.data
        password2= form.password2.data
        email = form.email.data
        new_user = User(f_name,l_name,email,password,password2)
        new_user.save_email
        new_user.save_password
        return redirect(url_for('dashboard'))
    return render_template('signup.html', form= form)