import json

txtjs = '''{
    "nome": "Vittori",
    "cognome": "Zuccala",
    "indirizzo" : {
        "via": "Via Orsola Rossi Maffiotti, 3",
        "citta": "Settimo T.se",
        "cap": 10136
    },
    "hobbies": ["diving","basketball"]
}'''

dictjs = {
    "nome": "Gianni",
    "cognome": "Rossi",
    "indirizzo" : {
        "via": "Via Marchettari, 3",
        "citta": "Milano",
        "cap": 10212
    },
    "hobbies": ["diving","basketball"]
}

nominativo = json.loads(txtjs)
dizionario = json.loads(json.dumps(dictjs, indent=2))       # dumps lo trasforma in stringa e poi lo devo caricare

print(nominativo["indirizzo"]["citta"])
print(dizionario["indirizzo"]["citta"])