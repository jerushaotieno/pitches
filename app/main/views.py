from app import app
from app import auth
from . import main
from flask_login import current_user, login_required
from flask import Flask, render_template,request,redirect,url_for,abort, flash
from ..models import User, Pitches, Comments
from .forms import UpdateProfile, PitchesForm, CommentsForm
from .. import db, photos

import os

from werkzeug.utils import secure_filename

from flask_sqlalchemy import SQLAlchemy



@main.route('/')
def index():
    return render_template('index.html')

@main.route('/home/')
def home():
    return render_template('home.html')

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main.route('/user/<uname>/update/pic',methods= ['GET','POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            path = f'uploads/{filename}'
            user.profile_pic_path = path
            db.session.commit()
            return redirect(url_for('main.profile',uname=uname))

    return 'add upload'        




@app.route('/', methods=["GET", "POST"])
def home():
    form = PitchesForm()
    if form.validate_on_submit():
        title = form.title.data
        category = form.category.data
        description = form.description.data

        # Updated review instance
        new_pitch = Pitches(title=title,category=category,description=description)

        # save review method
        new_pitch.save_pitches()
        return redirect(url_for('.home'))
    pitches= Pitches.query.all()

    return render_template("home.html", form=form, pitches=pitches)

# display pitches in one place
@main.route('/home/',methods = ['GET','POST'])
@login_required
def view():
    pitches= Pitches.query.all()
    return render_template('home.html', pitches=pitches)



app.route('/', methods=["GET", "POST"])
def home():
    form = CommentsForm()
    if form.validate_on_submit():
        comment = form.comment.data

        # Updated review instance
        new_comment = Comments(comment=comment)

        # save review method
        new_comment.save_comments()
        return redirect(url_for('.home'))
    comments= Comments.query.all()

    return render_template("home.html", form=form, comments=comments)

# display comments
@main.route('/home/',methods = ['GET','POST'])
@login_required
def views():
    comments= Comments.query.all()
    return render_template('home.html', comments=comments)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)