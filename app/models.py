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

    # id = db.Column(db.Integer,primary_key = True)
    # username = db.Column(db.String(255),index = True)
    # email = db.Column(db.String(255),unique = True,index = True)
    # # role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    # password_hash = db.Column(db.String(255))

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    # role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    pitches = db.relationship('Pitches',backref = 'user',lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read this attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'User{self.username}'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))



# for pitches

class Pitches(db.Model):

    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    title = db.Column(db.String(255))
    category = db.Column(db.String(255))
    description = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comment = db.relationship('Comments', backref = 'pitch', lazy = 'dynamic')

    def save_pitches(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls, id):
        pitches= Pitches.query.filter_by(id=id).all()
        return pitches

    def __repr__(self):
        return f'User{self.username}'



# for comments

class Comments(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    comment = db.Column(db.String(255))
    pitches_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))

    def save_comments(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, id):
        comments= Comments.query.filter_by(id=id).all()
        return comments

    def __repr__(self):
        return f'User{self.username}'