import datetime
import jwt
from ..extensions import db
from ..models import User
from ..config import Config


class UserHelper:
    @staticmethod
    def save_new_user(data):
        try:
            user = User.query.filter_by(
                username=data['username'].lower()).first()
            if not user:
                new_user = User(
                    name=data['name'].title(),
                    username=data['username'].lower(),
                    email=data['email'].lower(),
                    password=data['password']
                )
                db.session.add(new_user)
                db.session.commit()
                return True
            else:
                return None
        except Exception as e:
            raise e

    @staticmethod
    def auth_user(data):
        try:
            user = User.query.filter_by(
                username=data['username'].lower()).first()
            if user and user.verify_password(data['password']):
                return user
            else:
                return None
        except Exception as e:
            raise e

    @staticmethod
    def get_user_by_token(new_request):
        # get the auth token
        auth_token = new_request.headers.get('Authorization')
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if resp:
                user = User.query.filter_by(id=resp).first()
                if user:
                    response_object = {
                        'id': user.id,
                        'name': user.name,
                        'username': user.username,
                        'admin': user.admin
                    }
                    return response_object
                else:
                    return None
            else:
                return None
        else:
            return None

    @staticmethod
    def encode_auth_token(user_id):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'user_id': user_id
            }
            return jwt.encode(
                payload,
                Config.SECRET_KEY,
                algorithm='HS256'
            )
        except Exception as e:
            raise e

    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token, Config.SECRET_KEY, options={
                                 "verify_exp": False})
            return payload['user_id']
        except jwt.InvalidTokenError as e:
            raise e
