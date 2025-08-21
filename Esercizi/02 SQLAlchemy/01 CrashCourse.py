# Dal video: https://www.youtube.com/watch?v=529LYDgRTgQ
# E' un ORM (Object Relations Manager) per operazioni CRUD (Create, Read, Update, Delete)

import sqlalchemy as sa
import sqlalchemy.orm  as so # Questo modulo è per le Sessioni



################ METODO BASE DI UTILIZZO TRAMITE QUERY DIRETTE
engine = sa.create_engine('sqlite:///db_alchemy.sqlite',  echo= True)  # echo serve per fare debugging ed è prolisso
conn = engine.connect()

### Posso inserire direttamente del codice ma con il metodo text
# conn.execute(sa.text("CREATE TABLE IF NOT EXISTS people (id integer primary key, name varchar(50), age integer);"))
# conn.commit()
# conn.execute(sa.text("insert into people (name, age) values ('Vittorio', 50);"))
# conn.commit()
# cursor = conn.execute(sa.text("select * from people;"))
# print(cursor.fetchall())

# conn.close()

# # Le sessioni sono comode perchè permettono di inserire dei comandi tutti all'interno di una unica sessione
# session = so.Session(engine)
# session.execute(sa.text("CREATE TABLE IF NOT EXISTS camilli (name varchar(50));"))
# session.commit()
# session.close()



################ METODO AVANZATO DI UTILIZZO TRAMITE OGGETTI
# In questo caso, sono interessanti gli oggetti Metadata, Table, Column
# Poi posso avere diversi tipi di dati



meta = sa.MetaData()

people = sa.Table(
    "people",
    meta,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('name', sa.String, nullable=False),
    sa.Column('age', sa.Integer)
)

people.drop(engine, checkfirst=True)  # Messa questa istruzione per far rigirare il programma più volte
conn.commit()

meta.create_all(engine)


insert_statement = people.insert().values(name= 'Mike', age=30)
result = conn.execute(insert_statement)
conn.commit()

insert_statement = people.insert().values(name= 'Jane', age=40)
result = conn.execute(insert_statement)
conn.commit()

insert_statement = people.insert().values(
    [
        {'name': "Vittorio", 'age': 50},
        {'name': "Paola", 'age': 48},
        {'name': "Mauro", 'age': 35}
    ]
)
result = conn.execute(insert_statement)
conn.commit()

select_statement = conn.execute(people.select().where(people.c.age > 20))
for row in select_statement.fetchall():
    print(row.name)

##################### RELAZIONI
# Posso anche creare delle relazioni.
# Per esempio le persone possono avere diverse "cose" e quindi una relazione uno a molti

things = sa.Table(
    "things",
    meta,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('description', sa.String, nullable=False),
    sa.Column('value', sa.Float),
    sa.Column('owner', sa.Integer, sa.ForeignKey('people.id'))
)

things.drop(engine, checkfirst=True)   # Messa questa istruzione per far rigirare il programma più volte
conn.commit()


meta.create_all(engine)
insert_stat = things.insert().values(
    [
        {'description': 'Tomahowk', 'value': 34.4, 'owner': 1},
        {'description': 'Laptop', 'value': 800.4, 'owner': 1},
        {'description': 'Mouse', 'value': 21.5, 'owner': 1},
        {'description': 'Mouse', 'value': 12.4, 'owner': 2},
        {'description': 'Laptop', 'value': 340.4, 'owner': 1},
        {'description': 'Book', 'value': 11.1, 'owner': 2},
        {'description': 'Tomahowk', 'value': 34.4, 'owner': 2}
    ]
)
conn.execute(insert_stat)
conn.commit()


########################## JOINS
# Adesso che abbiamo dati in due tabelle possiamo fare i join
# INNER JOIN: join
# LEFT OUTER JOIN: outerjoin
join_statement = people.join(things, people.c.id == things.c.owner) 
select_statement = people.select().with_only_columns(people.c.name, things.c.description).select_from(join_statement)
selezione = conn.execute(select_statement)
print(selezione.fetchall())


######################### RAGGRUPPAMENTO
# Per raggruppare si utizza la funzione func
group_by_statement= things.select().with_only_columns(people.c.name, sa.func.sum(things.c.value)).select_from(join_statement).group_by(people.c.name).having(sa.func.sum(things.c.value) > 50)
selezione = conn.execute(group_by_statement)
for row in selezione.fetchall():
    print(row)

conn.close()

########################### SESSIONI
# Adesso andiamo a lavorare con le sessioni e non più con la connessione
# A questo punto invece dei metadata utilizziamo il declarative_base
# La cosa migliore che posso aggiungere record collegati in altre tabelle senza l'id ma direttamente con l'oggetto
engine_new = sa.create_engine('sqlite:///db_alchemy.sqlite',  echo= True)
Base = so.declarative_base()

class Person(Base):
    __tablename__ = "people"
    id = sa.Column(sa.Integer, primary_key=True)
    name =  sa.Column(sa.String, nullable=False)
    age = sa.Column( sa.Integer)
    things = so.relationship('Thing', back_populates='person')

class Thing(Base):
    __tablename__ = "things"
    id = sa.Column(sa.Integer, primary_key=True)
    description = sa.Column(sa.String, nullable=False)
    value = sa.Column(sa.Float)
    owner = sa.Column(sa.Integer, sa.ForeignKey('people.id'))
    person = so.relationship('Person', back_populates='things')


Base.metadata.create_all(engine_new)
Session = so.sessionmaker(bind=engine)
session = Session()

new_person = Person(name = 'Sam', age = 80)
session.add(new_person)
session.flush()     # Aggiunge temporaneamente la persona per poter fare il commit successivamente
                    # Non cambia nulla ancora nel database
new_thing = Thing(description = 'Desktop', value = 750.44, owner=new_person.id)
session.add(new_thing)
session.commit()

# A questo punto è facile accedere alla lista della tabella sottostante o sovrastante
print([t.description for t in new_person.things])
print(new_thing.person.name)

# Posso fare delle query
result = session.query(Person.name, Thing.description).all()
print(result)

result = session.query(Person.name, Person.age).filter(Person.name.startswith("M") )
print([p.name for p in result])

# Posso fare anche degli update
result = session.query(Thing).filter(Thing.value > 50).update({'description': 'Variabile'})
session.commit()

result = session.query(Thing.description, Thing.value).filter(Thing.value > 50).all()
print([t.description for t in result])


# Posso fare anche degli delete
result = session.query(Thing).filter(Thing.value > 50).delete()
session.commit()

result = session.query(Thing.description, Thing.value).filter(Thing.value > 50).all()
print([t.description for t in result])


# Per i groupby
result = session.query(Thing.owner, sa.func.sum(Thing.value)).group_by(Thing.owner).all()
print("Groupby:")
print(result)

####################################### PANDAS
# Molto utile l'utilizzo con pandas
import pandas as pd

df = pd.read_sql("SELECT * FROM people", con=engine_new)
print(df)

new_data = pd.DataFrame({'name': ['Florian', 'Jack'], 'age': [26,90]})
new_data.to_sql('people', con=engine_new, if_exists='append', index=False)


session.close()