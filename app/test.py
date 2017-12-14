#-*- coding: utf-8 -*

from flask import Flask, render_template, session, redirect, url_for, flash
from flask import request
from flask import current_app
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('What is your name', validators=[DataRequired()])
    submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

manager = Manager(app)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/net', methods=['GET', 'POST'])
def net():
    dev_type_list = [['网络设备', 'func1', 'func2'], ['接收机', 'func3', 'func4']]
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('net'))
    return render_template('net.html', dev_type_list=dev_type_list, name=session.get('name'), form=form)


@app.route('/rev')
def index3():
    return render_template('rev.html')


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
    # manager.run()
