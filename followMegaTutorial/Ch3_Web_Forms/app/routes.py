from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')

@app.route('/index')

def index():
    user = {'username':'Irene'}
    posts = [
        {
            'author':{'username':'John'},
            'body':'Beautiful day in Poland!'
        },
        {
            'author':{'username':'Susan'},
            'body':'The Avengers movie was so cool!'
        }
    ]
    #注意這裡寫的是給"index.html"
    return render_template('index.html', title = 'Home', user = user, posts = posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',title = 'Sign In', form = form)