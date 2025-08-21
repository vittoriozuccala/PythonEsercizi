class Person():
    def __init__(self, name, year):
        self.__name = name
        self.__birthYear = year
    def stampaNome(self):
        print(self.__name)


class Dipendente(Person):

    def impostaRAL(self, importo):
        self.__importo = importo
    def stampaRAL(self):
        print(self.__importo)
    

Vittorio = Person("Vittorio",1975)
Vittorio.stampaNome()

Zuccala = Dipendente("Zuccala", 1975)
Zuccala.impostaRAL(52000)
Zuccala.stampaRAL()
Zuccala.stampaNome()

diz = {'prova':
        {'camillo': 
         {'pippo':'pippino'}
        }
       }

print(diz['prova']['camillo']['pippo'])
diz = {}
diz['provina'] = 'pluto'
print(diz)

from datetime import datetime
dt = datetime.now().strftime('%#d %b %Y %H:%M')
print(dt)

risultato = [[1,2,3],[4,5,6]]
print(risultato[1:len(risultato)])


row = 'FCFILE_CCANALOG'
print(row.partition('_')[0])

import pandas as pd
df = pd.DataFrame(risultato)
import os
if os.path.exists("out.csv"):
   df.to_csv("out.csv",sep=';',index=False,header=False,mode='a') #,mode='a'
else:
   df.to_csv("out.csv",sep=';',index=False,header=['a','b','c'],mode='w') #,mode='a'

                    