
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/hello/<string:name>/")
def hello_user(name):
    return "Hello, %s" % name
app.run()
