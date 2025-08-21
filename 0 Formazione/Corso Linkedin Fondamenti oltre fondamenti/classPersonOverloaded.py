class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.__DataNascita = 0
  
  def stampaCaratteristiche(self, verifica = None):
    if verifica == "yes":
      print(self.name)
    else:
      print("Nessuna verifica")
  
  
  def annoNascita(self):
    self.__DataNascita = 2025-self.age
    return self.__DataNascita


class Dipendente(Person):
  def __init__(self, name, age):
    super().__init__(name, age)
    self.__RAL = 0
  
  def definisciRAL(self, ral):
    self.__RAL = ral
  
  def stampaRAL(self):
    print(f'La RAL è pari a {self.__RAL}')
  
  def stampaCaratteristiche(self, verifica=None):       # Metodo sovrascritto
    if verifica == "yes":
      print(f'Il nome del dipendente è {self.name}')
    else:
      print("Nessuna verifica")


Vittorio = Person("Vittorio",50)
Vittorio.stampaCaratteristiche()
Vittorio.stampaCaratteristiche("yes")

Luca = Dipendente("Luca",60)
Luca.definisciRAL(1000)
Luca.stampaRAL()
Luca.stampaCaratteristiche(verifica="yes")

