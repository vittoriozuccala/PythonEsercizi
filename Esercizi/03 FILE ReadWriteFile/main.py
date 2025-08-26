# Video: https://www.youtube.com/watch?v=Uh2ebFW8OYM

#########################Metdodo semplice
f = open('test.txt', 'r')
print(f"File {f.name} in modo {f.mode} ed è chiuso? {f.closed}")
f.close()
print("")

##########################Context Manager
#Il modo migliore è aprire il file in un contesto
#Permette di non inserire il metodo CLOSE()

with open('test.txt','r') as f:
    # rows = f.read() # Legge tutto il contenuto
    # print(rows)

    # rows = f.readlines()    # Legge le righe in un array
    # print(rows)

    # #Leggere tutte le righe in un colpo solo potrebbe andari in out of memory
    # #Per questo motivo con files grandi è meglio una riga per volta
    # for line in f:
    #     row = f.readline()
    #     print(row, end="")

    # #Potrei voler leggere un tot di righe alla volta
    # rows = f.read(100)
    # print(rows)

    # #Per tornare all'inizio del file utilizzo il metodo seek()
    # #Mentre il metodo tell() mi dice in che posizione sono
    # print(f.read(10))
    # f.seek(0)
    # print(f.read(10))
    # print(f.tell())
    pass

with open('prova.txt', 'w') as f:
    