from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class ContactForm(FlaskForm):
    name = StringField(label="name")
    email = StringField(label="email")
    message = StringField(label="message")
    submit = SubmitField("submit")


class LoginForm(FlaskForm):
    email = StringField(label="email", validators=[DataRequired()])
    password = StringField(label="password", validators=[DataRequired()])
    submit = SubmitField(label="login")

class SignupForm(FlaskForm):
    name = StringField(label="name", validators=[DataRequired()])
    email = StringField(label="email", validators=[DataRequired()])
    password = StringField(label="password", validators=[DataRequired()])
    cnf_password = StringField(label="Confirm password", validators=[DataRequired()])
    submit = SubmitField(label="Signup", validators=[DataRequired()])
