from . import bp

@bp.route('/')
def generate_token():

    return 'This is the main Blueprint on the server-side of this project.'