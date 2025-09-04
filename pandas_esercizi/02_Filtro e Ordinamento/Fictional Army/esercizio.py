import pandas as pd

#Crea un dizionario di esempio
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
            'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
            'deaths': [523, 52, 25, 616, 43, 234, 523, 62, 62, 73, 37, 35],
            'battles': [5, 42, 2, 2, 4, 7, 8, 3, 4, 7, 8, 9],
            'size': [1045, 957, 1099, 1400, 1592, 1006, 987, 849, 973, 1005, 1099, 1523],
            'veterans': [1, 5, 62, 26, 73, 37, 949, 48, 48, 435, 63, 345],
            'readiness': [1, 2, 3, 3, 2, 1, 2, 3, 2, 1, 2, 3],
            'armored': [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1],
            'deserters': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
            'origin': ['Arizona', 'California', 'Texas', 'Florida', 'Maine', 'Iowa', 'Alaska', 'Washington', 'Oregon', 'Wyoming', 'Louisana', 'Georgia']}

#Crea un dataframe
df = pd.DataFrame(raw_data)

#Imposta origin come indice
df.set_index('origin', inplace=True)

#Stampa le colonne veterans e deaths
df[['veterans','deaths']]

#Rappresenta deaths, size, deserters dal Maine ed Alaska
#        deaths  size  deserters
#origin
#Maine       43  1592          3
#Alaska     523   987         24
df.loc[['Maine','Alaska'],['deaths', 'size', 'deserters']]

#Seleziona le righe con deaths > 50
df.loc[df.deaths > 50,:]
df.query('deaths > 50')

#Seleziona le righe con deaths > 500 o < 50
df.query('deaths > 500 | deaths<50').sort_values('deaths', ascending=False)

#Seleziona i reggimenti che non siano Dragoons
print(df[df.regiment != 'Dragoons'])