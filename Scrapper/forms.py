from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from Scrapper.models import User

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists')


    def validate_email_address(self, email_address_to_check):
        email = User.query.filter_by(username=email_address_to_check.data).first()
        if email:
            raise ValidationError('Email already exists')


    username = StringField(label='User Name:',validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:',validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:',validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')

class LoginForm(FlaskForm):

    username = StringField(label='User Name:')
    password = PasswordField(label='Password:')
    login = SubmitField(label='Login')

class SearchForm(FlaskForm):
    search = StringField(label='search')
    button = SubmitField(label='make search')