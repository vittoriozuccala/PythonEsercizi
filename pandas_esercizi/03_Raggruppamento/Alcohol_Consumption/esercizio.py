import pandas as pd

drinks = pd.read_csv('drinks.csv')

#Quale continente beve più beer in media?
drinks.groupby('continent')['beer_servings'].mean().sort_values(ascending=False)
