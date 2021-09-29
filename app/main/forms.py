from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class LoginForm(FlaskForm):
    title = StringField('Login to comment and post',validators=[Required()])
    Name = TextAreaField('Add comment', validators=[Required()])
    submit = SubmitField('Submit')
