import pandas as pd


df = pd.read_csv('Euro_2012_stats_TEAM.csv', dtype={'Team': pd.StringDtype})

#Quanti teams hanno debuttato al Euro2012?
#16
df.count()['Team']

#Visualizza solo le colonne Team, Yellow Cards, Red Cards e assegna a discipline
#                   Team  Yellow Cards  Red Cards
#0               Croatia             9          0
#1        Czech Republic             7          0
#2               Denmark             4          0
discipline = df.loc[:, ['Team', 'Yellow Cards', 'Red Cards']]

#Calcola la media di cartellini gialli per team
#7.4
discipline.loc[:,'Yellow Cards'].mean()

#Filtra le squadre che hanno fatto più di 6 goals
#       Team  Goals
#5   Germany     10
#13    Spain     12
df.loc[df['Goals']>6, ['Team', 'Goals']]

#Seleziona i teams che iniziano con G
# Germany e Greece
df[df['Team'].str.startswith('G')]
df.query('Team.str.startswith("G")')

#Seleziona tutte le colonne a parte le ultime 3
df.iloc[:,0:-3]

#Rappresenta lo Shooting Accuracy di England, Italy, Russia
df.loc[:,['Team','Shooting Accuracy']].query('(Team == "Italy") | (Team == "England") | (Team == "Russia")')