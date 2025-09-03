# Soluzione del esercizio: https://www.youtube.com/watch?v=W8AB5s-L3Rw&list=PLgJhDSE2ZLxaY_DigHeiIDC1cD09rXgJv&index=5

import pandas as pd 
import os


#Leggi il file input
df = pd.read_csv("./utenti.txt", sep="|", index_col='user_id')

#Numero di osservazioni: 943
df.shape

#Nomi degli indici
df.index

#Dataype di ogni colonna
df.dtypes

#Stampa solo l'occupazione
df['occupation']

#Quante occupazioni ci sono: 21
len(df['occupation'].unique())

#Quale è la occupazione più frequente: student
occurrencies = df.groupby('occupation')['occupation'].count().sort_values(ascending=False) # Crea una pandas serie di occupazioni con il numero di occorrenze
maxOccurence = occurrencies.index[0] # Trova l'indice nella serie pandas con la massima occorrenza numerica
maxOccurence

#Summarize all columns
               #age occupation gender
#count   943.000000        943    943
#mean     34.051962        NaN    NaN
#std      12.192740        NaN    NaN
#min       7.000000        NaN    NaN
#25%      25.000000        NaN    NaN
#50%      31.000000        NaN    NaN
#75%      43.000000        NaN    NaN
#max      73.000000        NaN    NaN
#unique         NaN         21      2
#top            NaN    student      M
#freq           NaN        196    670
age_desc = df['age'].describe()
occ_desc = df['occupation'].describe()
gender_desc = df['gender'].describe()
join_desc = pd.concat([age_desc,occ_desc, gender_desc], axis=1)

join_desc

#Età media degli utenti: 34
df['age'].mean()