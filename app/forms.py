from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

class SignUpForm(FlaskForm):

    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    email = StringField('email', validators=[InputRequired()])
    password=StringField('email', validators=[InputRequired()])
    password2=StringField('email', validators=[InputRequired()])
    submit = SubmitField('Submit')