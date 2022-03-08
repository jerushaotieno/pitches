from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')