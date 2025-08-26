# Riferimenti

Video https://www.youtube.com/watch?v=AjsB6lM2-zw
Pagina installazione: https://duckdb.org/docs/installation/?version=stable&environment=cli&platform=macos&download_method=direct

# Tipologie databases

- OLTP sono transazionali fatti per scrivere bene in riga
- OLAP sono transazionali fatti per scrivere bene in colonna: DuckDB

# Limiti

- Utilizzabile su una sola macchina quindi non scalabile;
- Single user experience: non molto buono se si vuole accedere allo stesso file in più persone
- not for transactional: non va bene se si vuole aggiungere dati continuamente
- Read only for connection: per connessioni concorrenti deve essere a sola lettura

# Comandi

.open 'duck.db'
show tables;
describe table;

Per leggere da una cartella di CSV
SELECT _ FROM 'cartella/_.csv'
