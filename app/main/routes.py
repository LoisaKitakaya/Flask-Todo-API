import re
import os
import jwt
import smtplib
from . import bp
from uuid import uuid4
from functools import wraps
from app.extensions import db
from app.models.users import User, UserToken
from flask import render_template, redirect, url_for, flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

@bp.route('/')
def index():

    return render_template('index.html')

@bp.route('/contact/', methods=['GET', 'POST'])
def contact():

    return render_template('contact.html')

@bp.route('/signup/', methods=['GET', 'POST'])
def signup():

    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')
        password_2 = request.form.get('password_2')

        if not re.search("(^\w+)@([a-z]+)[.]([a-z]+\S)$", email):

            flash('Your email must be in the format of "abc@def.ghi", for example: example@email.com', "error")
            return redirect(url_for('main.signup'))

        try:

            email_already_in_use = User.query.filter_by(email=email).first()

        except:

            pass

        else:

            if email_already_in_use:

                flash("This email is already in use. Please choose a unique email.", "error")
                return redirect(url_for('main.signup'))

        if len(password) < 8 or len(password_2) < 8:

            flash("The password(s) provided is too short. Minimum characters expected for a strong password is 8.", "error")
            return redirect(url_for('main.signup'))

        if password != password_2:

            flash("The passwords provided do not match.", "error")
            return redirect(url_for('main.signup'))

        new_user = User(
            email=email,
            public_id=str(uuid4().hex),
            password=generate_password_hash(password, method='sha256')
        )

        try:

            db.session.add(new_user)

        except:

            flash('Something went wrong.', 'error')
            return None

        else:
            
            db.session.commit()
            flash(f'User account created successfully!', 'message')

            return redirect(url_for('main.login'))

    return render_template('signup.html')

@bp.route('/login/', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')

        try:

            this_user = User.query.filter_by(email=email).first()

        except:

            flash('Please check you email and try again.', 'error')
            return redirect(url_for('main.login'))

        else:

            if this_user == None:

                flash('Please check you email and try again.', 'error')
                return redirect(url_for('main.login'))
            
            if not check_password_hash(this_user.password, password):

                flash('Please check you password and try again.', 'error')
                return redirect(url_for('main.login'))

            login_user(this_user, remember=True)

            flash("Logged in successfully.", "message")
            return redirect(url_for('main.generate_token'))

    return render_template('login.html')

@bp.route('/logout/')
def logout():

    logout_user()

    flash("Logged out successfully.", "message")
    return redirect(url_for('main.login'))

@bp.route('/generate_token/', methods=['GET', 'POST'])
@login_required
def generate_token():

    KEY = os.environ.get('SECRET_KEY')

    try:

        has_token = UserToken.query.filter_by(user_id=current_user.id).first()

    except:

        user_token = None

    else:

        user_token = has_token

    if request.method == 'POST':

        access_token = jwt.encode(
            {'public_id': current_user.public_id},
            str(KEY),
            algorithm="HS256"
        )

        try:

            db.session.delete(UserToken.query.filter_by(user_id=current_user.id).first())

        except:

            pass

        else:

            db.session.commit()

        new_token = UserToken(
            token=str(access_token),
            user_id=current_user.id
        )

        try:

            db.session.add(new_token)

        except:

            raise

        else:

            db.session.commit()
            flash('Your token has been generated.', 'message')

        return redirect(url_for('main.generate_token'))

    return render_template('generate_token.html',\
        current_user=current_user, user_token=user_token)