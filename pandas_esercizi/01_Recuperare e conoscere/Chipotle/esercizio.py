"""Iniziamo a conoscere il nostro dataframe"""

import pandas as pd

def make_split(text: str):
    """
        Questa funzione permette di prendere un campo del dataframe,
        toglie le parentesi e lo splitta in modo da farlo diventare un array
    """
    text = text.replace("[","")
    text = text.replace("]","")
    text = text.split(",")
    return text

#Leggi il file CSV
df = pd.read_csv(
    "chipotle.txt", 
    sep = "\t",
    dtype={
        'item_name': pd.StringDtype(),
        'choice_description': pd.StringDtype()
        }
    )

#Sistema la base dati
df['item_price'] = df['item_price'].replace('\$|,', '', regex=True)
df['item_price'] = pd.to_numeric(df['item_price'])
df['choice_description'] = df['choice_description'].fillna(value="")
df['choice_description'] = df['choice_description'].apply(lambda x: make_split(x))


#Nomi delle colonne: ['order_id', 'quantity', 'item_name', 'choice_description','item_price']
df.columns

#Crea un campo revenue
df['revenue'] = df['quantity'] * df['item_price']

#Quanle è la media delle revenue?
df.groupby('order_id')['revenue'].sum().mean() 

#Quanti items sono stati venduti?
print(len(df['item_name'].unique()))
