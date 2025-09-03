# Scarica il file da 1Gb qui:
# https://www.kaggle.com/datasets/openfoodfacts/world-food-facts/data
import pandas as pd

df = pd.read_csv('en.openfoodfacts.org.products.tsv', sep="\t")

#Prime occurrenze
df.head()

#Dimensioni: 356.027, 163
df.shape

#Nomi colonne
#'code', 'url', 'creator', 'created_t', 'created_datetime',
#'last_modified_t', 'last_modified_datetime', 'product_name',
#'generic_name', 'quantity',
#'fruits-vegetables-nuts_100g', 'fruits-vegetables-nuts-estimate_100g',
#'collagen-meat-protein-ratio_100g', 'cocoa_100g', 'chlorophyl_100g',
#'carbon-footprint_100g', 'nutrition-score-fr_100g',
#'nutrition-score-uk_100g', 'glycemic-index_100g',
#'water-hardness_100g'
df.columns

#Quale è il nome della 105esima colonna? '-glucose_100g'
print(df.columns[104])

#Quale tipo di dati della colonna 105esima? dtype('float64')
df.dtypes[104]

#Quale è il product name della 19esima osservazione? Lotus Organic Brown Jasmine Rice
df.iloc[18]['product_name']

