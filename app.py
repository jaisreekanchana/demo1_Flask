
from flask import Flask,render_template
app=Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/j1/api/signin')
def user_signin():
    return"This is the signin page"


@app.route('/j1/api/login')
def user_login():
    return"This is an login page"


@app.route('/j1/api/about')
def user_about():
    return"About Us"


@app.route('/j1/api/blog')
def user_blog():
    return" view content"


if __name__=="__main__": 
    app.run(debug=True)