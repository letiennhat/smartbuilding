from flask import Flask, jsonify
import os
app = Flask(__name__)

@app.route('/<string>',methods = ["GET","POST"])
def index(string):
    with open(os.getcwd()+'/Blue_eyes/hide_on_push/emotion_values.txt','r+') as f:
        emotions = f.read()
    return jsonify(dict({
        'emotion':emotions
    }))
if __name__ == "__main__":
    app.run('0.0.0.0',8080,debug = 1)