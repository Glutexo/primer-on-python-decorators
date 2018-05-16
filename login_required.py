from functools import wraps
from flask import Flask, g, request, redirect, url_for

app = Flask(__name__)

@app.before_request
def before_request():
    g.user = None
    # g.user = 'user'


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/secret', methods=['GET'])
@login_required
def secret():
    return "success! secret"


@app.route('/login')
def login():
    return "success! login"