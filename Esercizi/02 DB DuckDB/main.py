# Dal video: https://www.youtube.com/watch?v=nWxwqxb0FCk
# DuckDB è un inline database process vuol dire che vive all'interno del processo.
# Non è un sostituto di MySQL o PostgresSQL ma di Pandas o sqlite
# Serve per un enorme mole di dati

import duckdb
import pandas as pd
import sqlite3

# conn = sqlite3.connect('db_sqlite.db')
# cur = conn.cursor()
# cur.execute("CREATE TABLE IF NOT EXISTS person (id INT, name TEXT);")
# cur.execute("INSERT INTO person (id, name) VALUES (1, 'Mike');")
# conn.commit()
# cur.close()
# conn.close()

# # Duckdb funziona nello stesso modo di sqlite nelle istruzioni
# conn = duckdb.connect('db_duckdb.db')
# cur = conn.cursor()
# cur.execute("CREATE TABLE IF NOT EXISTS person (id INT, name TEXT);")
# cur.execute("INSERT INTO person (id, name) VALUES (1, 'Mike');")
# conn.commit()
# cur.close()
# conn.close()

# ############## SIMILITUDINE CON PANDAS
# # DuckDB è simile a Pandas anche nelle funzioni
# # print(duckdb.read_csv('mydata.csv'))

# # Ma può fare molto di più
# print(duckdb.sql('SELECT * FROM mydata.csv'))

# Può leggere direttamente i dataframe di pandas
df = pd.read_csv('mydata.csv', sep=";")

print(duckdb.sql('SELECT * FROM df where age > 60'))

result = duckdb.sql('SELECT * FROM df where age > 60')
print(result.fetchall())

###################################################### INTERESSANTISSIMO
# Può popolare un db con il select
conn = duckdb.connect('db_duck_select.db')
conn.sql("CREATE TABLE IF NOT EXISTS people as SELECT * FROM 'mydata.csv';")
conn.commit()

print(conn.execute("SELECT * FROM people;").fetchall())


############################ Posso registrare un dataframe come tabelle ed usarlo come tale

df = pd.read_csv('mydata.csv', sep=";")
conn.register('persone', df)

print(conn.execute("select * from persone;").fetchall())



conn.close()
