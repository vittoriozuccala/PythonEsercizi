class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.__DataNascita = 0
    
  
  def stampaCaratteristiche(self):
    print('Name: {} , Age: {} '.format(self.name, self.age))
  
  def annoNascita(self):
    self.__DataNascita = 2025-self.age
    return self.__DataNascita