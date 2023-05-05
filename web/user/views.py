from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user

from web.db import db
from web.user.forms import LoginForm, RegistrationForm
from web.user.models import User
from web.utils import get_redirect_target

blueprint = Blueprint('user', __name__, url_prefix='/users')


@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(get_redirect_target())

    title = 'Log in'
    login_form = LoginForm()
    return render_template('user/login.html', page_title=title, form=login_form)


@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Logged in.')
            return redirect(get_redirect_target())

    flash('The username or password that you have entered is invalid.')
    return redirect(url_for('user.login', next=get_redirect_target()))


@blueprint.route('/logout')
def logout():
    logout_user()
    flash('Logged out.')
    return redirect(get_redirect_target())


@blueprint.route('/registration')
def registration():
    if current_user.is_authenticated:
        return redirect(get_redirect_target())

    title = 'Sign up'
    registration_form = RegistrationForm()
    return render_template('user/registration.html', page_title=title, form=registration_form)


@blueprint.route('/process-registration', methods=['POST'])
def process_registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, role='user', email=form.email.data)
        new_user.set_password(form.password.data)

        db.session.add(new_user)
        db.session.commit()

        flash('Your registration was successful!')
        return redirect(get_redirect_target())

    for field, errors in form.errors.items():
        for error in errors:
            flash(f'{getattr(form, field).label.text}: {error}')

    return redirect(url_for('user.registration', next=get_redirect_target()))
