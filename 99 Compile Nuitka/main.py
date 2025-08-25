# Video: https://www.youtube.com/watch?v=3WBoCeBkXqA
# Nuitka è un compilatore professionale
# Lavora su windows, linux, mac e senza avere files enormi

####################################### ATTENZIONE: non fattibile perchè:
# Bisognerebbe avere un gcc compiler
# La prima volta ti installa in automatico mingw64 oppure installarlo manualmente
# mingw64

# pip install nuitka
# pip install pyside6

# Per lanciare il compilatore:
# python -m nuitka main.py --onefile

import sqlalchemy as sa
import sqlalchemy.orm  as so # Questo modulo è per le Sessioni
import os



################ METODO BASE DI UTILIZZO TRAMITE QUERY DIRETTE
engine = sa.create_engine('sqlite:///db_alchemy.sqlite',  echo= True)  # echo serve per fare debugging ed è prolisso
conn = engine.connect()

### Posso inserire direttamente del codice ma con il metodo text
conn.execute(sa.text("CREATE TABLE IF NOT EXISTS people (id integer primary key, name varchar(50), age integer);"))
conn.commit()
conn.execute(sa.text("insert into people (name, age) values ('Vittorio', 50);"))
conn.commit()
cursor = conn.execute(sa.text("select * from people;"))
print(cursor.fetchall())

conn.close()

print(os.getcwd())

input('PREMI INVIO PER CHIUDERE LA FINESTRA')