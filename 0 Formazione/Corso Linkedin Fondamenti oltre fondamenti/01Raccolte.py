##########################################
# Le collection.
##########################################

# Il tipo più semplice sono le liste
# Le liste però non sono ordinate e ogni elemento richiamabile con un indice
# Ogni lista può contenere numeri, lettere e altro anche all'interno della stessa
guest = [
    'Maria',
    'Gordon',
    'Bob'
]

# La tupla è una lista ma immutabile

guest_tupla = (
    'Maria',
    15,
    True
)

# I dizionari, a differenza delle liste sono ordinate e richiamabili con una voce
californiaSymbols = {
    'Bird': 'Quail',
    'Animal': 'Greezly',
    'Flower': 'Poppy',
    'Fruit': 'Avocado'
}

print(guest[0])
print(californiaSymbols['Bird'])
print(guest_tupla[2])
print('\n')
input('PREMI UN TASTO PER FOR')

##########################################
# Iterazione attraverso le collection.
##########################################
spices = [
    'salt',
    'pepper',
    'cumin',
    'turmeric'
]

for spice in spices:
    print(spice)

print('\n')
input('PREMI UN TASTO PER WHILE')

i = 0
while i <= 100:
    print(i)
    i += 20