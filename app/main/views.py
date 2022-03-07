# from app import app
# from flask import render_template

# @app.route('/')

# def landing_page():
#     return render_template('index.html') 

# @app.route('/pitches')
# def home():
#     return render_template('pitches.html')

# @app.route('/pitches/<category>')
# def categories(category):
#     return render_template('categories.html') 

from app import auth
from . import main
from flask import render_template
from flask_login import login_required
from flask import render_template,redirect,url_for
from ..models import User
from .forms import RegistrationForm
from .. import db

@main.route('/')
def landing_page():
    return render_template('index.html')

@main.route('/pitches')
def home():
    return render_template('pitches.html')

@main.route('/pitches/<category>')
def categories():
    return render_template('categories.html') 

@main.route('/comments/<int:pitches_id>', methods=['GET','POST'])
@login_required
def pitch_comments(pitches_id):
    comments = pitch_comments.get_comments(pitches_id)
    return render_template('pitches.html', comments=comments)

