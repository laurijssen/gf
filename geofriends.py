import os
from flask import Flask, redirect, render_template, session, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(FlaskForm):
    name=StringField('Name?', validators=[DataRequired()])
    submitfield=SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True

        session['name]'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), known=session.get('known'))

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)
