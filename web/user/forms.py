from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from web.user.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={'class': 'form-control'})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'class': 'form-control'})
    remember_me = BooleanField('Remember me', default=True, render_kw={'class': 'form-check-input'})
    submit = SubmitField('Submit', render_kw={'class': 'btn btn-primary'})


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={'class': 'form-control'})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={'class': 'form-control'})

    password = PasswordField('Password', validators=[DataRequired()], render_kw={'class': 'form-control'})
    password2 = PasswordField('Confirm password',
                              validators=[DataRequired(), EqualTo('password', message='Passwords do not match.')],
                              render_kw={'class': 'form-control'})
    submit = SubmitField('Submit', render_kw={'class': 'btn btn-primary'})

    def validate_username(self, username):
        users_count = User.query.filter_by(username=username.data).count()
        if users_count > 0:
            raise ValidationError('Username already exist.')

    def validate_email(self, email):
        users_count = User.query.filter_by(email=email.data).count()
        if users_count > 0:
            raise ValidationError('User with this email already exist.')
