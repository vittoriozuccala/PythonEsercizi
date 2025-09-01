# Video https://www.youtube.com/watch?v=DkjCaAMBGWM
import sqlite3 as sq
import pandas as pd

db = sq.connect('pokemon.db')
cur = db.cursor()

query = "select * from pokemon;"

df = pd.read_sql_query(query,con=db)

# Data Import
# → pd.read_csv('file.csv')
# → pd.read_excel('file.xlsx')
# → pd.read_sql(query, conn)
# → pd.read_json('file.json')
# → pd.read_parquet('file.parquet')


# Visualizzazioni 
pd.set_option('display.max_rows', 100)
df.head(5) #inizio
df.tail(5) #fine
df.sample(5) #campione anche come df.sample(frac=0.1) o df.sample(frac=0.1, random_state=520)
df.columns
df.index

# Per vedere come sono i dati, ci sono una serie di metodi top down
# df.info()  # Sarebbe un describe table con non-null fields e tipo di dato con MEMORY USAGE. df.info(verbose=False) per sintesi
df.describe() # Per ogni campo dà il conteggio, media, devstd, min, max e clustes 25%, 50%, 75%
df[['Name']].describe() # Posso avere descrizione anche di un singolo campo
len(df) # len dice la lungehzza
df.shape # shape mi dice lunghezza e numero colonne

# slicing colonne
df[['Name', 'Total']]  # Lista in parentesi quadre
df[df.columns[:3]] # Le prime tre colonne
df[[c for c in df.columns if c.startswith('Sp.')]]  #MOLTO INTERESSANTE
df.select_dtypes('object') # selezionare solo gli int, float, text (object)

# slicing righe
# si usa iloc (usa gli indici) o loc(usa i nomi)
df.iloc[1,:]
df.iloc[:,[1,3]]
df.loc[:,['Name','Total']]

# Espressioni booleane
# Una delle funzioni più potenti è restituire un boolean da una espressione
df['Name'] == 'Bulbasaur' # Il primo True, gli altri False
df.loc[df['Name'] == 'Bulbasaur'] # Posso usarlo in loc
df.loc[(df['Name'] == 'Bulbasaur') | (df['Name'] == 'Volcanion')] # Posso combinare con & oppure | statment o TILDE per il not

# Query
# Posso usare anche un linguaggio simile a query
df.query('(Name.str.contains("saur")) and (Total > 10)')

# Summarize variabili numeriche
df['Attack'].mean()
df['Attack'].min()
df[['Attack', 'Total']].max()
df['Attack'].std()
df['Attack'].var()  # Varianza
df['Attack'].count()
df['Attack'].quantile([0.25,0.5,0.75])

df[['Attack', 'Total']].agg(['mean', 'min', 'max'])  # per avere più statistiche

# String Ops
# → df['col'].str.contains('pattern')
# → df['col'].str.extract('(\d+)')
# → df['col'].str.split(',', expand=True)

# Summarize variabili letterali
df['Name'].unique()
df['Name'].nunique()  #numero di univoci
df['Name'].value_counts()  #numero di univoci


# Metodi avanzati su colonne
df[['Total']].rank(method='dense')  #metodi dense o first (il primo della lista)
df[['Total']].shift(3)  # shifta in giù di uno. All'inizio o alla fine (-1) avrò dei Nun
df[['Total']].cumsum()   # Posso usare cummax, cumsum, cummin
df[['Total']].rolling(window=5).mean() # Molto interessante anche i rolling methods soprattutto con le date
df[['Total']].clip(50, 100)  # Non ho capito bene a cosa serva ma clippa tutti i valori tra 50 e 100
df[['Total']].clip(50, 100)

#Group by methods
df.groupby(['Type 1', 'Type 2'])[['Total', 'Attack']].mean()

#Pivot
df.pivot_table(values=['Attack', 'Total'], index='Name')

# Creare nuove colonne
df['Attack2'] = df['Attack'] / 2
df2 = df.assign(Attack3 = df['Attack']/3)  # In alternativa, posso creare un altro oggetto con il metodo assign
df2


# Sorting data
df.sort_values('Name', ascending=False).reset_index(drop=True)  #reset index resetta l'indice
df[['Name', 'Attack', 'Total']].isna().sum()     # Ritorna vero o falso nei valori NA di quelle colonne

#Drop/Fill data
# drop cancella tutti i valori che hanno NA nelle righe
df[['Name', 'Total']].dropna(subset=['Name'])
df[['Total']].fillna(df['Total'].mean())
df.drop_duplicates(subset=['Name'])   # Elimina i duplicati


#Replace
df['Name'].replace({'old':'new'})
# df['Name'].astype('Total')      # Non l'ho capita bene...

#Combining data
df1 = df.query('Name.str.contains("saur")')
df2 = df.query('Total >300')

dfStack = pd.concat([df1, df2], axis=0) #Axis 0 concatena uno sotto l'altro. Concat axis=1 concatena uno a fianco a l'altro
dfSide = pd.concat([df1.reset_index(drop=True), df2.reset_index(drop=True)], axis=1) #Axis 0 concatena uno sotto l'altro. Concat axis=1 concatena uno a fianco a l'altro
df1.shape, df2.shape, dfStack.shape, dfSide.shape   # Restituisce: (4, 14) (679, 14) (683, 14) (679, 28)


# Merge
df1= df.groupby(['Name'])['Total'].mean().reset_index()
df2= df.groupby(['Name'])['Attack'].mean().reset_index()
df2.merge(df1, how='inner')  #inner, outer, left, right

# Merge MOLTO PIU' UTILE
df3 = pd.merge(df2, df1, on=['Name'], how='left', suffixes=['_prima', '_dopo'])  # I suffissi sono utilizzati se vede lo stesso campo in entrambe



# Export
# → df.to_csv('output.csv')
# → df.to_excel('output.xlsx')
# → df.to_parquet('output.parquet')
# → df.to_json('output.json')