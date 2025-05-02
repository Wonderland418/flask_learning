#基本上route是在處理：當使用者開啟一個網址時，Flask要回應什麼東西給他
from flask import render_template
from app import app
@app.route('/')
#使用者打開index這頁時
@app.route('/index')
#flask做的事
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