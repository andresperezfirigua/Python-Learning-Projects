from flask_wtf import FlaskForm
from wtforms import StringField


class LoginForm(FlaskForm):
    email = StringField('Email')
    password = StringField('Password')
