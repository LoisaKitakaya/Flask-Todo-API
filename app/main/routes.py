import re
from . import bp
from uuid import uuid4
from app.extensions import db
from app.models.users import User
from flask import render_template, redirect, url_for, flash, request
from werkzeug.security import generate_password_hash, check_password_hash

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
            return redirect(url_for('todo.signup'))

        try:

            email_already_in_use = User.query.filter_by(email=email).first()

        except:

            pass

        else:

            if email_already_in_use:

                flash("This email is already in use. Please choose a unique email.", "error")
                return redirect(url_for('todo.signup'))

        if len(password) < 8 or len(password_2) < 8:

            flash("The password(s) provided is too short. Minimum characters expected for a strong password is 8.", "error")
            return redirect(url_for('todo.signup'))

        if password != password_2:

            flash("The passwords provided do not match.", "error")
            return redirect(url_for('todo.signup'))

        new_user = User(
            email=email,
            public_id=str(uuid4().hex),
            password=generate_password_hash(password, method='sha256')
        )

        try:

            db.session.add(new_user)

        except:

            raise

        else:
            
            db.session.commit()
            flash(f'User account created successfully!', 'message')

            return redirect(url_for('todo.login'))

    return render_template('signup.html')

@bp.route('/login/', methods=['GET', 'POST'])
def login():

    return render_template('login.html')

@bp.route('/generate_token/', methods=['GET', 'POST'])
def generate_token():

    return render_template('generate_token.html')