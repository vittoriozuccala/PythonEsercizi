# Best Practies

In questo file preso dal [video](https://www.youtube.com/watch?v=I2mWnh66Bkg) andiamo a vedere le best practise per fare un buon log

## Buon piano

Si abbia un buon piano.

- Quali sono i mein goals da loggare?
- Quali le operazioni critiche?
- Quali KPI si vogliono tracciare?

E' necessario fare un processo di revisione del log periodico
Riaggiustare i log levels è importante.
Bilanciare il rumore

## Logs level

E' importante utilizzare il livello giusto tra:

- INFO
- WARN
- ERROR
- FATAL

Ma soprattutto impostare un corretto livello di scrittura del log.
Si potrebbe ottenere _gigabytes_ di file di log

## Informazioni

Inserire tutte le informazioni **NON SENSIBILI** all'interno per poter leggere e comprendere il problema.
Meglio raccogliere più passaggi in una unica riga e non avere decine di righe per ogni processo.
Meglio mettere _access control_ o _criptazione dei logs_.

## Servizio di log

Un buon servizio di log è **BetterStock**

## Tempo di routine

Sarebbe meglio mettere un periodo di rotazione di circa 90gg.
