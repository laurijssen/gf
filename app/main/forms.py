from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name=StringField('Name?', validators=[DataRequired()])
    submitfield=SubmitField('Submit')
