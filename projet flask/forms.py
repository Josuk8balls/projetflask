from flask_wtf import FlaskForm
from wtforms import StringField

class LoginForm(FlaskForm):
    name = StringField('Name:', id='name')
    phone = StringField('Phone Number:', id='name')
    email = StringField('Email:', id='mail')
    job = StringField('Job Title:', id='name')
