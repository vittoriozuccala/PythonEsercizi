# Video https://www.youtube.com/watch?v=6_zPm84w_j4
# Base dati scaricata da https://www.kaggle.com/datasets

import pandas as pd
import matplotlib.pyplot as plt


# Operazioni preliminare: cambiare il tipo dati

df = pd.read_csv('titanic.csv', index_col='PassengerId', dtype={'Name':pd.StringDtype()}) 
#df.info()   # restituisce il tipo di dato, quanti non nulli ci sono ed i nomi colonna
            # i valori più complessi sono object ma se voglio attribuire un determinato tipo con la clausola dtype
df.columns

df.sum(numeric_only=True)

# Vediamo i grafici
# df['Age'].plot()
# df['Age'].plot(kind='hist')

# df['Pclass'].value_counts().plot(kind='pie')

# Group by cpon get_group
print(df.groupby('Pclass').get_group(3))

df.groupby('Pclass')['Survived'].mean().plot(kind='bar')
plt.show()

