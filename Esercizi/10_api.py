'''
SOAP: interfacce API via HTTP in XML
REST: interfacce API via HTTP in JSON
Utilizza 4 metodi principali
- GET: chiedo di leggere dati
- POST: chiedo di creare nuovi dati
- PUT: chiedo di modificare dati
- DELETE: chiedo di eliminarli

LE RICHIESTE E LE RISPOSTE SARANNO IN JSON

per richiedere la lettura dei dati del prodotto con id pari a 1, si invocherà una richiesta GET all’indirizzo www.mioservizioweb.org/api/prodotti/1
per richiedere la lettura dei dati di tutti i prodotti in offerta si invierà una GET all’URL www.mioservizioweb.org/api/offerte
per inserire i dati di un nuovo prodotto (ad esempio, un’app ad uso del personale del servizio) si invierà una POST all’indirizzo www.mioservizioweb.org/api/prodotti/nuovo
per modificare i dati del prodotto già esistente con id pari a 1 si invierà una PUT all’indirizzo www.mioservizioweb.org/api/prodotti/1
per cancellare il prodotto con id 1 verrà inviata una DELETE a www.mioservizioweb.org/api/prodotti/1

Il server gestisce gli stati:
200 “OK”: operazione eseguita con successo;
201 “Created”: successo con conseguente creazione di una nuova risorsa nel servizio. Ad esempio, potrebbe essere la risposta alla POST che inserisce un nuovo prodotto;
400 “Bad Request”: richiesta non formulata correttamente;
401 “Unauthorized”: è necessario eseguire prima un’autenticazione correttamente;
403 “Forbidden”: la richiesta sarebbe corretta ma si è chiesta una risorsa cui è vietato accedere;
404 “Not found”: risorsa non trovata. Immaginiamo ad esempio di inviare una GET all’indirizzo www.mioservizioweb.org/api/prodotti/999 ma il prodotto di id 999 non esiste nel database;
500 “Internal server error”: generico errore interno al server;
501 “Not implemented”: il tipo di richiesta non è stato implementato sul server.

Si può utilizzare flask
flask --app .\10_api.py run

'''


# Usando il plugin "Paste Json as Code"
# Si genera il seguente oggetto

# from uuid import UUID


# class Orchestratore:
#     id_operazione: int
#     id_progetto: int
#     messaggio: str
#     operazione_durata: int
#     operazione_fine: str
#     operazione_inizio: str
#     sessione_id: UUID
#     severity: int
#     dt_registrazione: str

#     def __init__(self, id_operazione: int, id_progetto: int, messaggio: str, operazione_durata: int, operazione_fine: str, operazione_inizio: str, sessione_id: UUID, severity: int, dt_registrazione: str) -> None:
#         self.id_operazione = id_operazione
#         self.id_progetto = id_progetto
#         self.messaggio = messaggio
#         self.operazione_durata = operazione_durata
#         self.operazione_fine = operazione_fine
#         self.operazione_inizio = operazione_inizio
#         self.sessione_id = sessione_id
#         self.severity = severity
#         self.dt_registrazione = dt_registrazione




from flask import Flask, jsonify, request

app = Flask(__name__)

incomes = [
    { 'description': 'salary', 'amount': 5000 }
]

@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route('/incomes')
def get_incomes():
    return jsonify(incomes)

# add new income
# curl -X POST http://127.0.0.1:5000/insertincomes -H "Content-Type: application/json" -d "{\"description\": \"Lottery\",  \"amount\": 1000}"  

@app.route('/insertincomes', methods=['POST'])
def add_income():
    incomes.append(request.get_json())
    
    data = request.get_json()
    print('Data Received: "{data}"'.format(data=data))
    return "Request Processed.\n"

@app.route('/orchestratore')
def get_orchestratore():
    import pyodbc
    conn = pyodbc.connect(
                     'Trusted_Connection=no',
                    driver='{SQL Server}',
                    server="svm-dwh.lingotto.local", 
                    database='Orchestratore')
    stringaSQL = "select top(10) * from Orchestratore.dbo.Lx_xJobActivity lxja"
    cursor = conn.cursor()
    cursor.execute(stringaSQL)
    desc = cursor.description
    riga = cursor.fetchone()
    column_names = [col[0] for col in desc]
    data = [dict(zip(column_names, riga))  
        for row in cursor.fetchall()]
    cursor.close()
    #print(data)
    return jsonify(data)

if __name__ == "__main__":
    app.run()
    #get_orchestratore()    


