from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Mingles'}
    posts = [
        {'author': {'username': 'Mingles'}, 'body': 'Blogging is cool!'},
        {'author': {'username': 'Selgnim'}, 'body': 'idk wat to put here...'}
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
