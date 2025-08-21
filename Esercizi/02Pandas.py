import pandas as pd

pokemon = pd.read_csv("FilesDati\\pokemon.csv")

# Leggere le prime sei righe
# La differenza tra loc ed iloc è che in loc devo mettere nome colonna mentre in iloc numero
# pokemon.loc[0, "Name"] mentre pokemon.iloc[0,0]
'''
print(pokemon.loc[0:5])
print(len(pokemon))

# Posso prendere le prime o ultime
print("Prendo prime 2")
print(pokemon.head(2))

print("prendo ultime due")
print(pokemon.tail(2))
'''

# Per le colonne uso la notazione liste
'''
print("Prendo colonna")
print(pokemon[['Name','HP']][0:3])
'''

# Ciclare
# iteritems: restituisce chiave/valore -- forse in disuso
# iterrows: restituisce riga per riga
# itertuples: tutta la riga come se fosse una tupla
'''
df2 = pokemon.head(2)
print("KEY")
for index,row in df2.iterrows():
    print(index)

print("VALUE")
for index,row in df2.iterrows():
    print(row)

print("COPPIA")
for index,row in df2.iterrows():
    print([index,row])
'''

# Come ordinare il DataFrame
'''
pokemon_sorted = pokemon.sort_index(ascending=False)
print(pokemon_sorted.head(4))


pokemon_sorted = pokemon.sort_values(by=["Type 1", "Name"], ascending=[False,True], na_position="last")
print(pokemon_sorted.head(4))
'''

# Come:
# aggiungere una colonna: insert(indice, nome, valore); loc[:,"Name"] = valore, assign(nome=valore)
# spostare una colonna: print loc iloc reverse subset di colonne df.columns.tolist()
# rimuovere una colonna: drop del e pop

# Aggiungere
'''
pokemon["Console"] = "Nintendo"
print(pokemon[["Name","Total","Console"]].head(3))


pokemon.insert(3,"Console","Nintendo")
print(pokemon.head(3))

pokemon.loc[:,"Console"] = "Nintento"  # su tutte le righe mette Console = Nintento al fondo
print(pokemon)


# Cancellare
print("TUTTO")
print(pokemon.head(4))
print("DROP")
pokemon.drop('Legendary', inplace=True, axis=1)  # Importante mettere axis= 0 sono le righe, axis = 1 sono le colonne
print(pokemon.head(4))
print("POP")
colonne = pokemon.pop("Name")
print(colonne.head(4))
'''

# Scrittura Excel
'''
pk = pokemon
pk2 = pokemon[["Name", "HP", "Total"]]
pk3 = pokemon.head(4)

with pd.ExcelWriter("nuovi_pokemon.xlsx") as writer:
    pk.to_excel(writer, sheet_name="Totali")
    pk2.to_excel(writer, sheet_name="Subset")
    pk3.to_excel(writer, sheet_name="Head")


import sqlite3
connection = sqlite3.connect("pokemon.db")
pokemon.to_sql(name='Pokemon', con=connection, if_exists="replace", index=False)
connection.close()
'''

# Filtrare i dati
# uguale, diverso, isin, str.contains, ><, &, |, ~
'''
df = pokemon
print("BULBASAUR")
print(df[df['Name'] == "Bulbasaur"])

print("CONTIENE SAUR")
print(df[df['Name'].str.contains("saur")])

print("BULBASAUR e VENUSAUR")
filtro = ['Bulbasaur','Venusaur']
print(df[df['Name'].isin(filtro)])


print("TOTAL > 700")
print(df[df['Total'] > 700])

print("CONCATENO CON & OPPURE |")
print(df[(df['Sp. Atk'] > 160) & (df['Total'] > 700)])  # Usare le parentesi quadre!!

print("QUERY")
print(df.query('Name.str.contains("saur")'))
'''

# Modificare i Dataframa
# Modificare in una o più colonne i dati con loc, multiple colonne, multipli valori, multiple condizioni
'''
pokemon.loc[pokemon.Name == 'Bulbasaur',['Name','HP']] = ['Babasauro',1000]
print(pokemon.head(2))
'''

# Raggruppare i dati con groupby
# Raggruppare una colonna per multiple colonne
# iterare i gruppi
# sum, mean, count, min, max, aggiungere una colonna count
'''
types = pokemon.groupby(['Type 1', 'Type 2'])
print(types.groups)  # Restituisce gli ID

for nome, gruppo in types:
    print(nome)
    #print(gruppo)


types2 = pokemon.loc[:,['Type 1', 'HP', 'Total']].groupby('Type 1').mean(numeric_only=True).sort_values(by='Total', ascending=False).head(5)
print(types2)
'''

# Pulire i dati
# Celle vuote, formato errato, dati errati, duplicati
pokemon.dropna(inplace=True)      # Elimina le righe con le celle vuote. Inplace lo sostituisce e riscrive
newpokemon = pokemon['Name'].fillna(value='Pippo')            # Riempie le celle vuote di Nome
# IMPORTANTE QUESTA FUNZIONE SOTTO
#newpokemon.Data = pd.to_datetime(campo del dataframe)

# Per i duplicati
# PEr vedere se ce ne sono:

print(pokemon.duplicated())

pokemon.drop_duplicates()