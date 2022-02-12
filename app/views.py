
from flask import redirect, render_template, url_for
from app import app
from .models import User , Credentials
from .forms import SignUpForm, LogInForm, Credential_log


User = User.User

app.config['SECRET_KEY'] = 'aSKh3r'

#Views
@app.route('/', methods=['GET','POST'])
def dashboard():

    
    mail= Credentials.Credentials.ac_email
    pword= Credentials.Credentials.ac_password
    acc= Credentials.Credentials.ac_type
    length = len(acc)
    form = Credential_log()
    
    if form.validate_on_submit():
        acc_type = form.acc_type.data 
        email = form.email.data
        password = form.password.data
        new_cred = Credentials.Credentials(acc_type,email,password)
        new_cred.save_credentials()
        
        

    title = 'Home - Welcome to The best Movie Review Website Online'

    return render_template('index.html',form=form , pword= pword, mail = mail, acc = acc, len=length)

@app.route('/login', methods=['GET','POST'])
def login():
    form= LogInForm()
    emails = User.user_email
    email = form.email.data
    password = form.password.data
    
    for i in range(0,len(emails)):
        if email == emails[i]:
            return redirect(url_for('dashboard'))

    return render_template('login.html',form=form)

@app.route('/signup',methods=['POST','GET'])
def sigup():
    form = SignUpForm()
    if form.validate_on_submit():
        f_name= form.first_name.data
        l_name = form.last_name.data
        password= form.password.data
        password2= form.password2.data
        email = form.email.data
        new_user = User(f_name,l_name,email,password,password2)
        new_user.save_email()
        new_user.save_password
        return redirect(url_for('login'))
    return render_template('signup.html', form= form)