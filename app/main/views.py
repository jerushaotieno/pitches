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
from flask import render_template,request,redirect,url_for,abort
from ..models import User
# from .forms import RegistrationForm, LoginForm
from .. import db

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/home/')
def home():
    return render_template('home.html')

# @main.route('/pitches/<category>')
# def categories():
#     return render_template('categories.html') 

# @main.route('/comments/<int:pitches_id>', methods=['GET','POST'])
# @login_required
# def pitch_comments(pitches_id):
#     comments = pitch_comments.get_comments(pitches_id)
#     return render_template('pitches.html', comments=comments)

# @main.route('/user/<uname>/update',methods = ['GET','POST'])
# @login_required
# def update_profile(uname):
#     user = User.query.filter_by(username = uname).first()
#     if user is None:
#         abort(404)

    # form = UpdateProfile()

    # if form.validate_on_submit():
    #     user.bio = form.bio.data

    #     db.session.add(user)
    #     db.session.commit()

    #     return redirect(url_for('.profile',uname=user.username))

    # return render_template('profile/update.html',form =form)

# @main.route('/user/<uname>/update/pic',methods= ['POST'])
# @login_required
# def update_pic(uname):
#     user = User.query.filter_by(username = uname).first()
#     if 'photo' in request.files:
#         filename = photos.save(request.files['photo'])
#         path = f'photos/{filename}'
#         user.profile_pic_path = path
#         db.session.commit()
#     return redirect(url_for('main.profile',uname=uname))