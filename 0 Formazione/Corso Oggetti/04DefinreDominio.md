# Definizione del dominio
Attività dopo le storie utente e gli use cases.

## Modello concettuale
Con l'analisi fatta, dobbiamo rappresentare gli obiettivi principali e le relazioni fra di loro.
Analizzando l'analisi cerchiamo di identificare prima di tutto gli oggetti.
Successivamente disegnare le relazioni che ci sono tra gli oggetti graficamente.
In ogni linea si scrive quale sia il tipo di relazione tramite un verbo.
Ad inizio e fine di ciascuna linea si mette la notazione 1-1 o 1-* o *-1 o *-*

## Identificare la responsabilità degli oggetti
Significa sapere cosa sono e cosa non sono gli oggetti.
Bisogna cercare di non dare troppe responsabilità ad un singolo attore 
Se continui a pensare al sistema con troppe responsabilità e non le distribuisci fra i vari oggetti, signifiica che stai ancora pensando come un programmatore procedurale: distibuire le responsabilità permette maggiore espansione e manutenzione nel tempo.

## Carte CRC
- Class
- Responsability
- Collaborators
Ogni scheda contiene la classe in testa e due colonne con responsabilità e collaborazione.
Per esempio per un videogioco con asteroidi e astronavi.
Meglio farlo su fogli di carta per cambiarli e ricambiarli molto velocemente.
Inoltre se aggiungi troppe righe ad una classe è sintomo che forse devi riprogettarla.

| Missile                                  |
| ---------------------- | ----------------|
| *Responsabilità*       | *Collaboratori* |
| vola nello spazio      | Navicella       |
| distrugge asteroide    | Area            |
| scompare oltre schermo | Asteroide       |

