from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length, Email, InputRequired, EqualTo


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), InputRequired()])
    email = StringField("Email", validators=[DataRequired() ,Email(), InputRequired(message="Please provide email")])
    message = TextAreaField("Message (max 900 char)" ,validators=[ DataRequired(), Length(1, 900), InputRequired()])
    submit = SubmitField("Send")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email(), InputRequired()])
    password = PasswordField("Password", validators=[DataRequired(), InputRequired()])
    rememberPassword = BooleanField("Remember Password", default=False)
    submit = SubmitField("Login")


class SignupForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), InputRequired()])
    email = StringField("Email", validators=[DataRequired(), Email(), InputRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(6,24), InputRequired()])
    cnf_password = PasswordField("Confirm password", validators=[DataRequired(), Length(6,24), InputRequired(), EqualTo('password', "password didn't match")])
    submit = SubmitField("Signup")


class AccountUpdateForm(FlaskForm):
    name = StringField("Update Name", validators=[DataRequired(), InputRequired()])
    email = StringField("Update Email", validators=[DataRequired(), Email(), InputRequired()])
    password = PasswordField("Update Password", validators=[DataRequired(), Length(6,24), InputRequired()])
    cnf_password = PasswordField("Confirm password", validators=[DataRequired(), Length(6,24), InputRequired(), EqualTo('password', "password didn't match")])
    submit = SubmitField("Update Details")
