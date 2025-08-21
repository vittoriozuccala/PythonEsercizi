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
Integrazione con Python:
https://pythonhosted.org/Flask-Bootstrap/
Temi free per Bootstrap:
https://bootswatch.com/
'''

from flask import Flask, render_template, url_for, request, session, redirect  # Le sessioni condividono dati tra pagine anche se non sicuro
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm    # Crea i forms
from wtforms import StringField, SubmitField, BooleanField, RadioField, SelectField, TextAreaField # Valida i forms
from wtforms.validators import DataRequired  # Importiamo i validatori
from flask-sqlalchemy
from flask-migrate 

app = Flask(__name__)
Bootstrap(app)          # Serve per creare siti più fiki

# Per motivi di sicurezza dobbiamo configurare delle chiavi
# per i forms
app.config["SECRET_KEY"] = "supersafekey" 

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

@app.route("/corsi/new")
def corso_new():
    return render_template("corso_new.html")

### Form base
@app.route("/corsi/created")
def corso_created():
    nome = request.args.get("corso-nome")
    oggetto = request.args.get("corso-oggetto")
    return render_template("corso_created.html", corso_nome=nome, corso_oggetto = oggetto)

### Form Avanzati lato backend
### Questo è un metodo più sicuro per fare i form
### Non paso le informazioni dal GET della pagina web ma tramite un POST che non fa vedere i dati
# Un altro vantaggio è che si possoino creare dei validatori
# Ma soprattutto posso fare direttamente una sicurezza dei campi per evitare la sql injection nel successivo accesso ai DB

#### Form complessi con validatori
#### Controllo la validità di una mail o di una password (per esempio reinseriscila) etc.

class FormCorso(FlaskForm):
    # Necessita di flask_wtf e fask_form
    name = StringField("Nome del corso", validators=[DataRequired()])
    teacher = StringField("Insegnante")
    is_active = BooleanField("Corso attivo?")
    difficulty =  RadioField(u"Difficoltà Corso", choices=[('id_facile','Facile'),('id_medio','Medio'),('id_avanzato','Avanzato')])
    platform = SelectField(u"Piattaforma di erogazione", choices=[('id_teams','Teams'),('id_zoom','zoom'),('id_meet','Meet')])
    feedback = TextAreaField()
    submit = SubmitField("Submit Form")


@app.route("/corsi/create/simple", methods=["GET", "POST"])
def advance_course():
    name = False
    teacher = False
    is_active = False
    difficulty = False
    platform = False
    feedback = False
    form = FormCorso()

    if form.validate_on_submit():
        session["name"] = form.name.data
        session["teacher"] = form.teacher.data
        session["is_active"] = form.is_active.data
        session["difficulty"] =  form.difficulty.data
        session["platform"] = form.platform.data
        session["feedback"] = form.feedback.data

        # RESET
        form.name.data = ""
        form.teacher.data = ""
        form.is_active.data = ""
        form.difficulty.data = ""
        form.platform.data = ""
        form.feedback.data = ""

        return redirect(url_for('corso_created'))

    return render_template(
        "corso_simple.html", 
        corso_simple_form = form, 
        corso_nome = name, 
        corso_teacher = teacher,
        course_active = is_active,
        course_difficulty = difficulty,
        course_platform = platform,
        course_feedback = feedback)



if __name__ == "__main__":
    # Posso mettere debug=True per fare il debugging
    app.run(debug=True)