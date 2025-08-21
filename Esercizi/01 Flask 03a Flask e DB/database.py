from main import db, Corsi, app

# Creazione delle tabelle
app.app_context().push()
db.create_all()

corso_flask = Corsi("Flask", "Andrea", 10)
corso_pygame = Corsi("Pygame", "Mario", 20)


# Aggiungiamo alla sessione del database i nostri oggetti
db.session.add_all([corso_flask,corso_pygame])

# Committiamo la transazione
db.session.commit()

print("ID corso flask: ", corso_flask.id)
print("ID corso Pygame: ",  corso_pygame.id)
