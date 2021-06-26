from flask import request
from app.api.errors import bad_request, resource_exist, error_response
from app.helpers import UserHelper, ValidationHelper


def login():
    try:
        data = request.get_json() or {}
        validation = ValidationHelper(
            data,
            {
                'username': {
                    'required': True
                },
                'password': {
                    'required': True
                }
            }
        ).valid()

        resp_obj = {}

        if validation['is_valid']:
            user = UserHelper.auth_user(data)
            if user:
                resp_obj = {
                    'token': UserHelper.encode_auth_token(user.id),
                    'user': {
                        'name': user.name,
                        'email': user.email,
                        'username': user.username,
                    }
                }
            else:
                resp_obj = {
                    'status': 'failed',
                    'message': 'Invalid username/password.'
                }

            return resp_obj
        else:
            return bad_request(validation['messages'])
    except Exception as e:
        print(e)
        return error_response(500)


def register():
    try:
        data = request.get_json() or {}
        validation = ValidationHelper(
            data,
            {
                'name': {
                    'required': True
                },
                'username': {
                    'required': True
                },
                'email': {
                    'required': True,
                    'email': True
                },
                'password': {
                    'required': True
                }
            }
        ).valid()

        if validation['is_valid']:
            if UserHelper.save_new_user(data):
                resp_obj = {
                    'status': 'success',
                    'message': 'User successfully created.'
                }
                return resp_obj
            else:
                return resource_exist('username')
        else:
            return bad_request(validation['messages'])

    except Exception as e:
        print(e)
        return error_response(500)
