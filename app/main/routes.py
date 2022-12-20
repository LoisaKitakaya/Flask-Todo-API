from flask import render_template
from . import bp

@bp.route('/')
def index():

    return render_template('index.html')

@bp.route('/about/')
def about():

    return render_template('about.html')

@bp.route('/contact/', methods=['GET', 'POST'])
def contact():

    return render_template('contact.html')

@bp.route('/signup/', methods=['GET', 'POST'])
def signup():

    return render_template('signup.html')

@bp.route('/login/', methods=['GET', 'POST'])
def login():

    return render_template('login.html')

@bp.route('/generate_token/', methods=['POST'])
def generate_token():

    pass