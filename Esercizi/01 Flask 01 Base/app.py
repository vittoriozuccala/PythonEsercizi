'''
Moduli necessari:
- flask
- flask_wtf
- wtforms
- flask-sqlalchemy
- flask-migrate
- flask-restful
- flask-jwt
- bandit
- black


########################## CARTELLE
Tutte le app flask hanno due cartelle:
- static (immagini, icone, css)
- templates 

########################## SITI ACCATTIVANTI
Si può partire da questo sito che permette la creazione di siti interessanti:
https://getbootstrap.com/
'''

from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)          # Serve per creare siti più fiki

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/esempio_jinja")
def esempio_jinja():
    return render_template("flask.html")

@app.route("/corsi/<name>")
def corsi(name):
    corsi = ['flask', 'python', 'api']
    return render_template("corsi_flask.html",nome_corso = name, lista_corsi = corsi)


@app.route("/info")
def info():
    return "<h2>Un sacco di informazioni</h2>"

@app.errorhandler(404)
def page_not_found(errore):
    return render_template("404.html"), 404     # Importante: unico caso in cui gli devo dire anche codice errore


if __name__ == "__main__":
    # Posso mettere debug=True per fare il debugging
    app.run(debug=True)