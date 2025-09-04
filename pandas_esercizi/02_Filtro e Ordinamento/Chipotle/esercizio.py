import pandas as pd

#Leggi il file
df = pd.read_csv('chipotle.txt', sep="\t")

#Pulisci il campo item_price
df['item_price'] = df['item_price'].replace('\$|,', '', regex=True)
df['item_price'] = pd.to_numeric(df['item_price'])


#Quanti prodotti costano più di 10$?
#clean the item_price column and transform it in a float
#reassign the column with the cleaned prices
#delete the duplicates in item_name and quantity
#select only the products with quantity equals to 1
# df_unique = df[['item_name', 'item_price']].groupby(['item_name'],level=0).mean().sort_values('item_name')

#################Risultato
#item_name          item_price
#6 Pack Soft Drink  12.98          1
#Barbacoa Bowl      11.48          6
#                   11.49          1
#                   11.75         20
#Barbacoa Burrito   11.08          1
#                                 ..
#Veggie Burrito     11.25         32
#                   33.75          1
#Veggie Salad Bowl  11.25         10
#Veggie Soft Tacos  11.25          2
#                   16.98          1
df.query('item_price >= 10').sort_values('item_price').groupby(['item_name','item_price'])['order_id'].count()


#Quale è il prezzo di ogni item
# delete the duplicates in item_name and quantity
# select only the products with quantity equals to 1
# select only the item_name and item_price columns
# sort the values from the most to less expensive

############################# Risultato
#                item_name  item_price
#3350     Steak Salad Bowl       11.89
#1229  Barbacoa Salad Bowl       11.89
#1311     Steak Salad Bowl       11.89
#606      Steak Salad Bowl       11.89
#2610  Carnitas Salad Bowl       11.89
df.drop_duplicates().query('quantity == 1').sort_values('item_price', ascending=False)[['item_name', 'item_price']]

#Qual'è la quantità dell'item più costoso ordinato?
#################Risultato:
#item_name     Chips and Fresh Tomato Salsa
#item_price                           44.25
#quantity                                15
df[['item_name', 'item_price', 'quantity']].sort_values('item_price', ascending=False).iloc[0]

#Quante volte è stato ordinato il Veggie Salad Bowl?
#==> Veggie Salad Bowl    18
df.loc[df['item_name'] == 'Veggie Salad Bowl',['order_id','item_name']].drop_duplicates().groupby('item_name')['order_id'].count()

#Quante volte è stato ordinato più di un Canned Soda?
# 20
df.loc[df['item_name'] == 'Canned Soda', ['item_name', 'order_id', 'quantity']].query('quantity > 1').count()