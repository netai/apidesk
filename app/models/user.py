import datetime
from ..extensions import db, bcrypt


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(100), index=True,
                         unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password_hash = db.Column(db.String(128),  nullable=False)
    registered_on = db.Column(
        db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    @property
    def password(self):
        raise AttributeError('password not readable')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password, 10)

    def verify_password(self, pwd):
        return bcrypt.check_password_hash(self.password_hash, pwd)

    def __repr__(self):
        return '<User {}>'.format(self.username)
