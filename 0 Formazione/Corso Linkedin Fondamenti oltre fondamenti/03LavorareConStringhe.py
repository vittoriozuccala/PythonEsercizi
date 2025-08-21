# Concatenazione con un +

# value = input('Inserisci un numero: ')
value = '50'
print('Il numero inserito: ' + value)

# Guardare se il nome e cognome hanno la prima lettera maiuscola
firstName = 'vittorio'
lastName = 'zuccala'
note = 'award: Nobel Peace Prize'

firstName = firstName.capitalize()      # Questi metodi sono per le stringhe

print(firstName)
lunghezzaNote = len(note)
print(lunghezzaNote)
print('award è sito in: '+ note[7:lunghezzaNote])

# Sono molto importanti le espressioni regolari
# /hello/           cerca un testo specifico
# \d \w             qualsiasi digit o lettera
# .                 qualsiasi carattere
# + o *             + per una o più occorrenze; * per nessuna o più occorrenze
# ?                 indica 0 o 1 occorrenza
# {n}               un numero di occorrenze

import re
fiveDgtZip = '98101'
nineDgtZip = '98101-0003'
phoneNumber = '234-567-8901'

fdz = r'\d{5}'
ndz = r'\d{5}-\d{4}'
print(re.search(fdz, fiveDgtZip))
print(re.search(ndz, nineDgtZip))