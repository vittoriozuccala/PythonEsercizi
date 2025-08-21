'''
Questo file è generato dal video https://www.youtube.com/watch?v=DSG6KGF4qJQ
'''

import configparser as cp

config = cp.ConfigParser(
    interpolation= cp.ExtendedInterpolation()     # Utile per la interpolazione delle opzioni
)

try:
    config.read("FilesDati\\configurazione.ini")
except:
    print("File di configurazione in errore")
    raise SystemExit()

# Posso accedere con la notazione dei dizionari
# oppure con la funzione get
# Nel metodo ho l'opzione fallback che mi dà un valore di default
print(config["DATABASE"]["server"])
print( config.get("LOG" , "dir") )
print( config.get("DATABASE" , "archive_dir") )
print( config.get("DATABASE" , "porticina", fallback=666) )

# Il metodo GET ha diverse varianti come:
# config.getboolean
# config.getfloat
# config.getint

# Posso sapere le sezioni e le opzioni in una sezione
print( config.sections() )
print( config.options("DATABASE") )

# Posso verificare l'esistenza di un parametro
if ("username" in config["DATABASE"]):
    print("username exists")