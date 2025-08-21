import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy.dialects.sqlite

BASEDIR = os.path.abspath(os.path.dirname(__name__))  # Recupero la directory nella quale mi trovo

app = Flask(__name__)

# Configurare il path del db ed alcune informazioni
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASEDIR, 'static', 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

# Aggiungiamo SQLALchemy alla applicazione
db = SQLAlchemy(app=app)


# Per ogni tabella dobbiamo definire una classe
# Definiamo i corsi
class Corsi(db.Model):
    # Nome tabella
    __tablename__ = 'corsi'

    # Definizione struttura tabella
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text)
    insegnante = db.Column(db.Text)
    allievi = db.Column(db.Integer)
    
    # Definire il costruttore
    def __init__(self, nome, insegnante, allievi):
        self.nome = nome
        self.insegnante = insegnante
        self.allievi = allievi

    # Definisco il REPR per printare ogni volta che viene chiamato l'oggetto
    def __repr__(self):
        message = f"Corso {self.nome} insegnato da {self.insegnante} con numero allievi {self.allievi}"
        return message


if __name__ == "__main__":
    app.run(debug=True)