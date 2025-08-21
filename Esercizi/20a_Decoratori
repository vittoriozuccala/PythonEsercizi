'''
Come funzionano i decoratori
Capisce che gli passo il parametro successivo (in questo caso una funzione)

Sono delle funzioni che estendono il funzionamento di altre funzioni senza modificarne il comportamento
'''


##############################################################################################################

# Primo caso. Estende le funzionalità di do_this e do_that 

##############################################################################################################
import time

def tictoc(fct) -> None:
    def wrapper() -> None:
        t1 = time.time()
        fct()
        t2 = time.time()-t1
        print(f'{fct.__name__ } ran in {t2} seconds')
    return wrapper

@tictoc
def do_this():
    time.sleep(1.3)

@tictoc
def do_that():
    time.sleep(0.4)


do_this()
do_that()
print("Done")

##############################################################################################################

# Secondo caso. Estende le funzionalità di get_ice_cream 

##############################################################################################################

def add_sprinkles(func):
    def wrapper(*args, **kwargs):   # Si definisce un'altra volta il wrapper senza parametri    
                                    # Il wrapper è indispensabile perchè altrimenti, nel codice, appena vedo il decoratore, 
                                    # faccio partire la funzione
                                    # Mettendo *args, **kwargs copro ogni casistica
        print("**You add sprinkles 😊!!**")
        func(*args, **kwargs)       # Anche qui devo mettere i parametri variabili
    return wrapper

@add_sprinkles
def get_ice_cream(flavor: str) -> None:
    # Non abbiamo parametri
    print(f'This is your {flavor} ice cream 🍨')

get_ice_cream("vanilla")