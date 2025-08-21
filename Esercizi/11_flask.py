'''
Questo tutorial arriva dal video: https://www.youtube.com/watch?v=pXMwAD9zMeg
Il sito di riferimento di Flask: https://flask.palletsprojects.com/en/stable/
'''

from flask import Flask, jsonify, request, render_template
from markupsafe import escape

app = Flask(__name__)

importi_valori = [
    {"nome": "Vittorio", "importo": 100},
    {"nome": "Marco", "importo": 80},
    {"nome": "Luca", "importo": 70}
]

# importi_valori = ["1","2","3","4","5"]


@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/importi")
def importi():
    return render_template('importi.htm', lunghezza = len(importi_valori), importiTot=importi_valori)


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

app.run(use_reloader = True, debug = True)