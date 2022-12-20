from flask import render_template
from . import bp

@bp.route('/tokens/')
def tokens():

    return render_template('tokens.html')