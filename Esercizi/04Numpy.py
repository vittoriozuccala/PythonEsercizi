# E' una libreria per lavorare con gli array
# Sono delle liste ma 50 volte più veloci e con tante funzionalità
# Numerical Python
# https://www.w3schools.com/python/numpy/default.asp


# pip install pyinstaller
# pyinstaller 04Numpy.py --onefile

import numpy as np
# La differenza grande tra liste ed array è questa:
'''
arrBase = np.array([1,2,3,4,5])
lista = [1,2,3,4,5]

print(arrBase*5)
print(lista*5)
'''

# Creare array 0D, ... 5D
# ndim, definire dimensione
# arrange, zeros, ones
'''
arr0D = np.array(42)
arr2D = np.array([[1,2,3],[4,5,6]])
arr3D = np.array([
    [[1,2,3],[4,5,6]],
    [[7,8,9],[10,11,12]]
])

arr5D = np.array([1,2,3], ndmin=5)

print(arr5D)
print(arr5D.ndim)

arrArange = np.arange(5,50,5)
arrZero = np.zeros((3,2))
arrOne = np.ones(5)

print(arrArange)
print(arrZero)
print(arrOne)
'''

# Inizializzare array
# 0D...5D
# Indicizzazione negativa
'''
arr3D = np.array([
    [[1,2,3],[4,5,6]],
    [[7,8,9],[10,11,12]]
])
print(arr3D[1,0,2])
print(arr3D[1,0,-2]) # indicizzazione negativa
'''

# Slicing di array
# da x a y, da x alla fine, dall'inizio a x
# 2D, 3D
''' 
arr3D = np.array([
    [
        [1,2,3,4,5],[4,5,6,7,8]
    ],
    [
        [7,8,9,10,11],[10,11,12,13,14]
    ]
])

print(arr3D[1,0,3:])

print(arr3D[1,0,0::2])  # Parti da zero fino alla fine e salti ogni due elementi
'''

# Tipi di dati
# numpym, dtype per controllare
# creare array con tipo, astype
# Documentazione: https://www.w3schools.com/python/numpy/numpy_data_types.asp
'''
arr1D = np.array([1,2,3,4,5,6,7,8,9,10])
arr1DText = np.array(["a","b","c"])         #dtpe <U1
print(arr1D.dtype)
print(arr1DText.dtype)

arr1DS = np.array([1,2,3,4,5], dtype='S')  # Lo creo direttamente con un tipo di dati specifico
print(arr1DS.dtype)

arrText = np.array(["1","2","3"])
arrInt = arrText.astype('i')               # Posso convertirlo dopo
print(arrInt+4)
'''

# Copy e View: entrambi copiano un array in un altro
# Mentre copy fa una copia effettiva tipo fotocopia, view ne fa una sorta di link ma le modifiche fatte da una parte si rifanno anche dall'altra parte
# differenze, copy, view, check se è proprietario dei dati
'''
arr = np.array([1,2,3])     # è il proprietario
arrCopy = arr.copy()        # è una copia scollegata
arrView = arr.view()        # è una vista che cambia con il proprietario

arr[0] = 10

print(arr)
print(arrCopy)
print(arrView)

print(arr.base)             # non ha una base (è proprietario)
print(arrCopy.base)         # non ha una base (è proprietario)
print(arrView.base)         # ha come base arr (NON è proprietario)
'''

# Shape e Reshape
# Cosa è la shape: arr.shape
# Cosa è la reshape (view), 1d-2d, 1d-3d, possiamo fare sempre reshape?
# dimesioni sconosciute, spianare l'array (flattering)
'''
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
arr2D = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])

print(arr.shape)            # indica un array a i dimensione con 12 elementi
print(arr.reshape(-1))      # Reshape è una view. Questo comando manda a schermo l'array
print(arr.reshape(4,3))     # Restituisce un array a 4 elementi da 3 numeri ciascuno (2 dimensioni)
print(arr.reshape(2,3,2))   # Restituisce un array a 2 elementi da 3 ciascuno con 2 numeri ciascuno (3 dimensioni)
print(arr.reshape(2,-1,3))  # Il -1 dice a numpy di creare lui la dimensione compatibile

print(arr2D.flatten())      # Trasforma più dimensioni in una soltanto
'''

# Iterare gli array
# Iterare 1D, 2D, 3D
# nditer, campiare tipo di dato, iterare a step, prendere indice ndenumerate
'''
arr = np.array([1,2,3,4,5,6])
arr2d = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
for x in arr:
    print(x)

for x in arr2d:
    for y in x:
        print(y)

# Se si vuole fare in una volta sola si usa nditer (lo faccio n volte su d dimensioni)
for x in np.nditer(arr2d, flags=['buffered'], op_dtypes=['S']):      # Prende tutti gli elementi. Il flags permette di fare quello che voglio 
    print(x)                                                         # od_types restituisce il tipo di dato voluto (stringa in questo caso)

for x in np.nditer(arr2d[:,1::2]):
    print(x)

for i,x in np.ndenumerate(arr2d):                   # Permette di printare sia l'indice sia il valore
    print(f'{i} con valore {x}')
'''

# UNIRE GLI ARRAY
# concatenate 1D,2D
# stacking stack, hstack, vstack, dstack
'''
arr1 = np.array([[1,2,3], [7,8,9]])
arr2 = np.array([[4,5,6], [10,11,12]])

arrConcat = np.concatenate((arr1,arr2), axis=1)       # Concatenazione. Axis omesso vale 0 altrimenti posso specificare
arrStack = np.stack((arr1,arr2), axis=1)              # Non definendo axis va a staccare uno dietro l'altro con una dimensione aggiuntiva - Prenderà 1 e 4!!!
arrHstack = np.hstack((arr1,arr2))                    # Fa la stessa cosa di concatenate. Sotto gruppo di stack
arrVstack = np.vstack((arr1,arr2))                    # Fa la stessa cosa di stack dim=1. Sotto gruppo di stack


print(arrConcat)
print(arrStack)
print(arrHstack)
print(arrVstack)
'''

# DIVIDERE GLI ARRAY
# array_split e split per 1D e 2D
# split sugli assi, vsplit, hsplit, dsplit
'''
arr = np.array([1,2,3,4,5,6])
arr2 = np.array_split(arr,2)            # Splitta in due gli array. Lo split andrebbe in errore se si eccedono il numero degli split

arrDoppio = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
arrDoppio2 = np.array_split(arrDoppio,3)

print(f'Array2 {arr2}')
print(f'ArrayDoppio {arrDoppio2}')

'''
# CERCARE, FILTRARE (numero, pari, dispari), ORDINARE
# cercare con where (ritorna indici)
# ordinare con sort 1D, 2D (ritorna nuovo array)
# filtrare con esempio statico, dinamico e scorciatoia
'''
arr = np.array([1,2,3,4,5,4,4,9,8,7])
arrIndici = np.where(arr == 4)
arrSorted = np.sort(arr)

# Filtro semplice
filtro = [False,False,True,False,True,True,False,True,False,True]
arrFiltered = arr[filtro]

print(arrIndici)
print(arrSorted)
print(arrFiltered)
'''

# RANDOM
# randint, rand, generate random array 
# choice per estrarre valore e generare array
# data distribution con probabilità
# shuffle (agisce su array) e permutation (ritorna nuovo array)
'''
x = np.random.randint(100)  # Numero random tra 0 e 100
y = np.random.rand()  # Numero random tra 0 e 1

array1D = np.random.randint(100, size = (5))

print(x)
print(y)
print(array1D)

arr = np.array([1,2,3,4,5,6,7,8,9,10])
numerocasualeinarray = np.random.choice(arr)
print(numerocasualeinarray)

arrChoice = np.random.choice(arr, p=[0.01, 0.09, 0.2, 0.01, 0.01,0.01,0.07,0.05,0.05,0.5 ], size=(3,2)) # Aggiungo la probabilità con numeri che sommati fanno 1
print(arrChoice)

np.random.shuffle(arr)  #mischia gli elementi dello stesso array altrimenti utilizzo permutation per crearne uno nuovo
print(arr)
'''

# UFUNC
# cosa sono, vedere tipo funzione, creazione di proprie
# add, divide, multiply, power, subtract, mod/reminder, trunc, ceil, floor
# Sono funzioni che agiscono su ndarray  che ci permettono di fare operazioni
'''
arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(type(np.add))

def addCinque(x):
    return x + 5

addCinque = np.frompyfunc(addCinque, 1, 1) # La registriamo e diciamo che abbiamo un elemento in input ed uno in output

print(addCinque(arr))
'''