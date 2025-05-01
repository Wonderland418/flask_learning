from flask import Flask
app = Flask(__name__)

#routing

@app.route('/')
def home():
    return 'Welcome to the Home Page!'

@app.route('/about')
def about():
    return 'This is the About Page.'

#view functions

@app.route('/greet/<name>')
def greet(name):
    return f'Hello,{name}!'

#request object

from flask import request

#由於只允許用POST方式進入，如果用GET進入會報錯"Method Not Allowed"
@app.route('/submit' , methods = ['POST'])
def submit():
    username = request.form.get('username')
    return f'Hello,{username}!'

#輸入submit的頁面，submit必須由此存取
@app.route('/submit_for_user')
def submit_for_user():
    return '''
        <form action = "submit" method = "POST">
            <input name = "username">
            <input type = "submit">
        </form>
    '''
#response object

from flask import make_response

@app.route('/custom_response')
def custom_response():
    response = make_response('This is a custom response!')
    response.headers['X-Custom-Header'] = 'Value'
    return response