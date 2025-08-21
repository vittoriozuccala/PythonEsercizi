# Le caratteristiche sono proprietà
# I metodi sono i comportamenti dell'oggetto
# Per creare un oggetto utilizzo una classe
# Su una classe possiamo creare più oggetti istanziandoli con proprietà e metodi differenti


class Persona:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.dataNascita = 2025-self.age
  
  def stampaCaratteristiche(self):
    print('Name: {} , Age: {} '.format(self.name, self.age))

p1 = Persona("John", 36)

print(p1.name)
print(p1.age)
print(p1.dataNascita)

p1.stampaCaratteristiche()


# Adesso provo ad importate il file classPerson e ad istanziare un oggetto persona
import classPerson
personaNuova = classPerson.Person("Vittorio",50)
personaNuova.stampaCaratteristiche()

AnnoDiNascita = personaNuova.annoNascita()
print(AnnoDiNascita)

