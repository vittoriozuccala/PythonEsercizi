# Le classi sono aggregate quando una vive dentro l'altra
# ma entrambe possono vivere senza ciascuna di esse
# Un esempio è la libreria ed il libro
# La libreria vive indipendentemente dal libro ma il libro è contenuto nella libreria

class Book:
    def __init__(self, title, pages):
        self.Titolo = title
        self.Pagine = pages

    def __repr__(self):
        return f"Libro {self.Titolo} con {self.Pagine} pagine"
    
class Library:
    def __init__(self, name, year: int, bk=None):
        self.Nome = name
        self.Anno = year 
        self.Libri = bk

b1 = Book("Jumanji", 200)
b2 = Book("Il Signore degli Anelli", 400)
b3 = Book("Aceronte",122)

books = [b1,b2,b3]

lib = Library("Biblioteca Nazionale", year="pippo", bk=books)


print(b1)