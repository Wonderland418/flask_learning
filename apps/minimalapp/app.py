from flask import Flask
app = Flask(__name__)

@app.route("/") #裝飾器，告訴Flask哪個URL應該觸發下面的函數。在這裡是指定根URL
def index(): #定義一個名為index的函數，調用於當用戶訪問根URL時
    return "Hello, Flaskbook!"

@app.route("/hello")
def hello():
    return "Hello,World!"

if __name__ == '__main__':
    app.run(debug = True)