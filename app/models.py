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
from flask_login import UserMixin
from . import login_manager


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    # role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read this attribute')

    @password.setter
    def password(self, password):
        self.password_encrypt = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_encrypt, password)

    def __repr__(self):
        return f'User{self.username}'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


