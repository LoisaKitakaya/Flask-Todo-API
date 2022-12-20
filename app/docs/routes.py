from flask import render_template
from . import bp

@bp.route('/docs/')
def docs():

    return render_template('docs.html')