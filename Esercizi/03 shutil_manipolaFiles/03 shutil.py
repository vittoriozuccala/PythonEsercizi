#Video: https://www.youtube.com/watch?v=sXzezIK0d7c
#Modulo builtin per manipolare files
#Documentazione: https://docs.python.org/3/library/shutil.html

import shutil

################################Copia/Spostamento di un file e cartelle
#Come copiare un file in modo veloce
# shutil.copy('first.txt', 'second.txt')
# shutil.move('first.txt', 'cartella_destination/third.txt')

#Per copiare una directory
# shutil.copytree('cartella_source', 'cartella_destination')

#Interessante ignorare specifici files
# def ignore_files(directory,files):
#     """Restituisce un elenco di files da ignorare nella copia"""
#     return [f for f in files if f.endswith('d.txt')]
#oppure un pattern tipo return [f for f in files if 'invocie' in f]

# shutil.copytree('cartella_source', 'cartella_destination2', ignore=ignore_files)

# shutil.rmtree('source_dir)

#E' possibile copiare anche i metadati
# shutil.copystat('first.txt', 'second.txt')
#Oppure copiare il file direttamente con gli stessi metadati
# shutil.copy2('first.txt', 'second.txt')


##############################Cambiare la ownership
# shutil.chown('first.txt', user="pippo")


###############################Trovare un comando
# print(shutil.which('python'))


###############################Si possono creare e scompattare archivi
# shutil.make_archive('myarchive', 'zip', 'cartella_source')
# shutil.unpack_archive('myarchive.zip', 'unpacked_dir')
#Per vedere i formati supportati
print(shutil.get_archive_formats())
print(shutil.get_unpack_formats())

#Per inserire altri formati (non coperto da video), si può usare
#shutil.register_archive_format()

################################Memoria del disco
(total, used, free) = shutil.disk_usage("/")
print(f"Totali: {total/1000000000} Gb")


