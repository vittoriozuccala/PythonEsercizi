#Navigare system,
#Move files
#Get proprierties

import os
from datetime import datetime

###########################Stampa tutti gli attributi e metodi del modulo
# print(dir(os))

#########################Directorys
print(os.getcwd())      # Stampa la directory dove ci troviamo
# os.chdir('C:/Users/n219547/OneDrive - Santander Office 365')    # Change directory
# print(os.getcwd())
# print(os.listdir()) # Lista file e directory
# os.makedirs('OS-MODULE')    # Crea la cartella con eventuale albero delle cartelle
# print(os.listdir()) # Lista file e directory
# os.removedirs('OS-MODULE')   # Rimuove le directory recursivamente altrimenti rmdir


#########################Rename
# os.rename('file.txt', 'out.txt')   # Anche qui c'è il renames per il recursivo

########################Informazioni
# mod_time = os.stat('out.txt').st_mtime
# print(os.stat('out.txt'))
# print(datetime.fromtimestamp(mod_time))

######################Camminare tra le directory
#walk genera delle tuple di tre elementi
#(directory, directory nel path, files nel path)
# for dir_path, dirnames, filenames in os.walk('.'):
#     print('Current Path: ', dir_path)
#     print('Directories: ', dirnames)
#     print('Files: ', filenames)
#     print()

##########################HOME DIRECTORY
# environment = os.environ
# print(environment)
# print()
# print(os.environ.get('HOME'))


#######################CONCATENARE PATH
file_name = 'file.txt'
print(os.getcwd() + file_name)      # ATTENZIONE: in questo modo mi perdo gli slash
print(os.path.join(os.getcwd(), file_name))

print(os.path.basename('./directory_name/fileinside.txt'))  # Mi dice il base path
print(os.path.split('./directory_name/fileinside.txt'))  # Splitta il file dalla cartella
print(os.path.splitext('./directory_name/fileinside.txt'))  # Splitta il nome del file in nome e estensione
print(os.path.exists('./directory_name/fileinside.txt'))  # check exists
print(os.path.isdir('./directory_name/fileinside.txt'))  # check isdir or isfile

print(dir(os.path)) # vedere metodi nel modulo