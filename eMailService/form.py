from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField

from wtforms import validators, ValidationError

class InputForm(Form):

    email = TextField("Email",validators=[validators.InputRequired(), validators.Email(message='Enter valid email address')])

    message = TextAreaField("Message",validators=[validators.InputRequired(message='Enter message')])

    submit = SubmitField("Send")