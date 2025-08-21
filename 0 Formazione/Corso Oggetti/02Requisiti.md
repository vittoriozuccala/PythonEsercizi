# Requisiti
La prima cosa è la raccolta requisiti.

La descrizione dei requisiti non ha nulla a che fare con la OOP ma solo la descrizione delle esigenze.
Questa fase non deve contenere parole come classe, ereditarietà, astrazione o altri tecnicismi.

Comprendere le necessità e cosa dovrebbe fare l'applicazione.
Ci sono alcuni requisiti di cui tenere sempre conto:
- Aspetti legali (immagazzina dati sensibili, sanitari o bancari o altro?)
- Performance (quanto tempo ci mette a compiere una azione)
- Support (in caso non funzioni alle 4 del mattino, cosa bisogna fare?)
- Sicurezza: cosa succede in caso di hack? E' un requisito importante?

Il cliente può avere solo una vaga idea di cosa vuole.
Prenditi il tempo per capire bene di cosa necessità l'utente.

## Requisiti funzionali
- Devi esplicitare *cosa la applicazione DEVE fare*

Per un forno microonde spaziale, l'applicazione DEVE:
- riscaldare il cibo
- permettere all'utente di impostare un orario di riscaldamento
- avvertire l'utente che il cibo è riscaldato

Poi si descrivono i requisi non-funzionali ovvero *come l'applicazione DOVREBBE essere*
Ovvero il mantenimento, la disponibilità, affidabilità, usabilità.
- Il sistema deve essere disponibile 24/7
- Utilizzabile mentre si indossano i guanti
- NO (è un requisito eccessivo. All'inizio concentrati sui requisiti assolutamente indispensabili): Compatibile con windows, ios, android

Dividi i requisiti in:
- **Must to have**
- **Should have**


## FURPS requirements
Di solito i requisiti vengono divisi in:
- Functionality (è ciò che l'utente vuole):
  - Capability
  - Reusability
  - Security
- Usability (influisce sulla persona che utilizzerà il programma):
  - Estetica
  - Documentazione
  - Consistency
  - User friendly
- Reliability
  - Avaliability (ogni quanto è disponibile e tempistiche)
  - Failure Rate & Duration
  - Predictability (tempo di recupero dopo che il sistema è off)
- Performance:
  - Speed
  - Efficienza
  - Resource consumption
  - Scalability
- Supportability:
  - Testability
  - Extensibility
  - Serviceability
  - Configurability


## Esempio
Creare un jukebox per astronauti dove ogni astronauta può inserire brani.
Se un astronauta inserisce più di tre brani alla coda, un altro astronauta che inserisce un brano andrà come terzo nella coda soppiantando quella precedente

### Functionality (must do)
Descrivere un jukebox.
Deve mantenere la lista di brani.
Deve permettere di far scorrere la lista dei brani.
Deve permettere di far suonare la musica.
Deve avere un bottone per selezionare l'artista ==> deve permettere all'utente di ordinare per artista
Deve identificare l'utente senza specificare come (sarà altro requisito)
Crea una coda e ad ogni brano associa l'utente che ha aggiunto il brano
Ogni volta che un utente inserisce un brano alla coda verifica quanti brani ci sono di quell'utente
Se un secondo utente inserisce un brano lo inserisce in coda a meno che non ci siano più di tre brani in coda di altro utente ed a quel punto lo inserisce come quarto

### Usability (should be)
Intuitivo da usare mentre gli astronauti fluttuano
Deve essere disponibile 24/7
Deve richiedere poca energia
Deve essere aggiornabile come playlist
