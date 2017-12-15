#-*- coding: utf-8 -*
from flask import Flask, render_template, session, redirect, url_for, flash, request, current_app
from flask_script import Manager
from flask_bootstrap import Bootstrap
from datetime import datetime
from . import main
from .forms import NameForm
# from .. import db
# from ..models import User


@main.route('/')
def index():
    return render_template('base.html')


@main.route('/net', methods=['GET', 'POST'])
def net():
    dev_type_list = [['网络设备', 'func1', 'func2'], ['接收机', 'func3', 'func4']]
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('.net'))
    return render_template('net.html', dev_type_list=dev_type_list, name=session.get('name'), form=form)


@main.route('/rev')
def rev():
    return render_template('rev.html')

