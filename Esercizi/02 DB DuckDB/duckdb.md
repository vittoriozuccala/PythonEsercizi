# Riferimenti

Video https://www.youtube.com/watch?v=AjsB6lM2-zw
Pagina installazione: https://duckdb.org/docs/installation/?version=stable&environment=cli&platform=macos&download_method=direct

# Estensioni

- [Core Extension](https://duckdb.org/docs/stable/extensions/overview.html)
- [Community Extension](https://duckdb.org/community_extensions/list_of_extensions)

# Tipologie databases

- OLTP sono transazionali fatti per scrivere bene in riga
- OLAP sono transazionali fatti per scrivere bene in colonna: DuckDB

# Limiti

- Utilizzabile su una sola macchina quindi non scalabile;
- Single user experience: non molto buono se si vuole accedere allo stesso file in più persone
- not for transactional: non va bene se si vuole aggiungere dati continuamente
- Read only for connection: per connessioni concorrenti deve essere a sola lettura

# Comandi

Generare un set di dati per i test

```sql
    CALL dbgen(sf=0.1);
```

.open 'duck.db'
show tables;
describe table;

Per leggere da una cartella di CSV

```sql
SELECT _ FROM 'cartella/_.csv'
```

# Client

Per lanciare una serie di comandi prima di iniziare la sessione

```bash
    duckdb -init FILENAME
```
