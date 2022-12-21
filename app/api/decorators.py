import os
import jwt
from functools import wraps
from flask import request, jsonify, make_response
from app.models.users import User

def token_required(func):

    @wraps(func)
    def decorator(*args, **kwargs):

        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:

            token = request.headers['x-access-token']

        # return 401 if token is not passed
        if not token:

            return make_response(jsonify({'message' : 'Token is missing !!'}), 401)
  
        try:

            # decoding the payload to fetch the stored details
            data = jwt.decode(token, str(os.environ.get('SECRET_KEY')), algorithms="HS256")
            current_user = User.query\
                .filter_by(public_id = data['public_id'])\
                .first()
                
        except:

            return make_response(jsonify({
                'message' : 'Token is invalid !!'
            }), 401)

        # returns the current logged in users context to the routes
        return  func(current_user, *args, **kwargs)
  
    return decorator