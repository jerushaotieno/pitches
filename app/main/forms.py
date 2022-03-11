from wtforms import SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')


# content to display using the pitches form
class PitchesForm(FlaskForm):
    username = TextAreaField('Give your username',validators = [DataRequired()])
    title = TextAreaField('What is your pitch about e.g. sales?.',validators = [DataRequired()])
    description = TextAreaField('Give your pitch here.',validators = [DataRequired()])
    category = SelectField(u'Select Pitch Category', choices=[('....Select Category', 'Select Category.....'), ('Technology', 'Technology'), ('Business', 'Business'), ('Health', 'Health')])
    submit = SubmitField('Submit')


# content to display using the comments form
class CommentsForm(FlaskForm):
    username = TextAreaField('Give your username',validators = [DataRequired()])
    comment = TextAreaField('Add your comment here',validators = [DataRequired()])
    submit = SubmitField('Submit')