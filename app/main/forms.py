from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required
from ..models import User
from wtforms import ValidationError

class EditProfile(FlaskForm):
    about = TextAreaField('Tell us about yourself.',validators = [Required()])
    submit = SubmitField('Update')


class UpdatePost(FlaskForm):
    text = TextAreaField('Edit post here',validators = [Required()])
    submit = SubmitField('Update')


class QuoteForm(FlaskForm):
    quote_text = TextAreaField('Your quote here', validators=[Required()])
    submit = SubmitField('Post')


class CommentForm(FlaskForm):
    quote_comment = TextAreaField('Make a comment', validators=[Required()])
    submit = SubmitField('Comment')
