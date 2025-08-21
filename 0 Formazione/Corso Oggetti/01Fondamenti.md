# Fondamenti
Si utilizza UML (Unified Modelling Language) prima di qualsiasi riga di codice.

## Gli oggetti
Per pensare ad un oggetto nella programmazione basta pensare ad un oggetto nel mondo reale.
Un oggetto può essere anche qualcosa di intangibile come una data, un timer o un conto bancario.
Per capire se qualcosa sia rappresentabile come oggetto basta chiedersi se ha un nome come una cosa, una persona, un luogo fisico, un concetto.


Ogni oggetto ha:
- identità: ogni oggetto anche se ha la stessa classe è diverso da un altro
- caratteristiche che descrivono lo stato dell'oggetto:
  - possono essere chiamate **attributi, caratteristiche, campi, stati, variabili**
  - alcune sono fisse: la dimensione di una tazza o il suo colore
  - alcune sono variabili: come la quantità di liquido all'interno di una tazza
- comportamenti:
  - sono delle azioni, dei verbi che descrivono azioni

## Le classi
Le classi definiscono gli oggetti.
E' una descrizione dettagliata.
Si possono creare differenti oggetti su una stessa classe.
Ogni classe ha:
- un nome: definisce il nome della classe e cosa sia
- attributi: descrivono la classe
- comportamenti: cosa può fare l'oggetto

## Concetti base
Ci sono quattro concetti base quando si parla di OOP definiti **APIE**
- Abstraction:
  - Se dico persona si sa di cosa stiamo parlando senza pensare ad una persona specifica
  - Non creo classi separate per ciascuna persona
- Polymophism:
  - Usa le stesse interfacce per metodi in differenti tipi di oggetti
  - Posso avere la caffettiera classica e quella francesce. Gli input e output sono i medesimi (caffè ed acqua ==> caffè liquido) ma il procedimento è differente
  - Nel caso sopra descritto, il metodo infusione viene modificato
    - **Method overriding** descrive il polimorfismo dinamico ovvero la riscrittura dei metodi
    - **Method overloading** descrive il polimorfismo statico. Il metodo ha lo stesso nome ma con differente numero di parametri:
      - brew(coffe, water) e brew(tea, water) restituiscono output differenti
- Inheritance:
  - Una classe può ereditare attributi e metodi da un'altra classe
  - Posso riutilizzare il codice: utilizzo la classe Person con attributi e metodi in comune e derivo Dipendente e Cliente per le specificità
  - L'ereditarietà in UML si segna con una freccia dal figlio al padre con linea continua e freccia chiusa
  - La classe padre si chiama *super class* e la derivata *child class*
  - E' possibile anche che una Child Class derivi da più Super class anche se può apparire qualcosa di confusionario
- Encapsulation
  - riguarda gli elementi di un oggetto
  - alcuni attributi non possono essere gestiti dall'esterno ma soltanto all'interno della classe: *si devono usare i metodi della classe*
  - Alcuni attributi possono essere quindi nascosti e accessibili soltanto tramite un metodo


## Ereditarietà in Python
```python
class Veicolo:
    def __init__(self, marca):
        self.marca = marca

    def descrizione(self):
        return f"Questo è un veicolo di marca {self.marca}"

class Automobile(Veicolo):
    pass
```

## Approccio
L'approccio alla OOP consiste in 5 fasi:
- **Raccolta requisiti**: capiamo cosa dobbiamo fare
- **Descrivi l'applicazione**: in un discorso colloquiale descrivi cosa deve fare la applicazione e come useranno l'applicazione le persone
- **Identifica gli oggetti più importanti**: è necessario identificare e quindi descrivere con proprietà e metodi gli oggetti principali
- **Descrivi le interazioni**: descrivi come gli oggetti devono e possono interagire fra di loro
- **Crea un diagramma di classe**: è una visualizzazione grafica della classe