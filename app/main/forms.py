from wtforms import SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')


# content to display using the pitches form
class PitchesForm(FlaskForm):
    username = TextAreaField('Give your username',validators = [DataRequired()])
    title = TextAreaField('Give your pitch a title.',validators = [DataRequired()])
    description = TextAreaField('Describe what your pitch is about.',validators = [DataRequired()])
    category = SelectField(u'Select Pitch Category', choices=[('....Select Category', 'Select Category.....'), ('Technology', 'Technology'), ('Business', 'Business'), ('Health', 'Health')])
    submit = SubmitField('Submit')


# content to display using the comments form
class CommentsForm(FlaskForm):
    username = TextAreaField('Give your username',validators = [DataRequired()])
    comment = TextAreaField('Add your comment here',validators = [DataRequired()])
    submit = SubmitField('Submit')