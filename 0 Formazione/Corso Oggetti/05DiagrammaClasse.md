# Diagramma di classe
Adesso è il momento in cui Inheritance e Polymorfism possono entrare in gioco.
Si utilizza UML diagram

Ogni classe deve essere nominata al singolare.

| Classe                                                    |
| --------------------------------------------------------- |
| attributoPrimo: String                                    |
| attributoSecondo: Integer                                 |
| attributoTerzo: Coordinate                                |
| attrubutoSOTTOLINEATO (significa globale se underlined)   |
| --------------------------------------------------------- |
| + metodoPrimo()                                           | + è visibile
| + metodoSecondo(Integer): ritorna Integer                 | + è visibile
| - metodoTerzo(Coordinate): ritorna Booleano               | - non visibile all'esterno


## IMPORTANTE
Può capitare che si scriva una classe e si istanzino molti oggetti.
A quel punto ci si accorge che manca un attributo e/o un metodo.
Aggiungerlo vorrebbe dire ricreare tutti gli oggetti allora lo si fa globale (per la classe ma non per il resto del programma) e per richiamarlo lo si fa con la classe.attributo anzichè oggetto.attributo
Chiaramente se cambio il valore di quella variabile globale, cambia nello stesso modo in tutti gli oggetti istanziati.

```python
class Spaceshift():
    # Class variable
    toughness = 0.85

    def __init__(self):
        # Resto del codice

# A quel punto, se non ho capito male la si richiama dal codice
navicella = Spaceshift()

# Ma non nell'oggetto ma nella classe
Spaceshitf.toughness = 0.90
```

