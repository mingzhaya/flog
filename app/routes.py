from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Mingles'}
    posts = [
        {'author': {'username': 'Mingles'}, 'body': 'Blogging is cool!'},
        {'author': {'username': 'Selgnim'}, 'body': 'idk wat to put here...'}
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('A login was requested for user ' + form.username.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)
