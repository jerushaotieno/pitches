# class Pitch:
#     '''
#     '''
#     def __init__(self, pitch_text, pitch_category, pitch_author):
#         '''
#         '''
#         self.pitch_text=pitch_text
#         self.pitch_category=pitch_category
#         self.pitch_author=pitch_author

from . import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_encrypt=db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('You can only read this attribute')

    @password.setter
    def password(self, password):
        self.password_encrypt = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_encrypt, password)

    def __repr__(self):
        return f'User{self.username}'
