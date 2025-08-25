# Video: https://www.youtube.com/watch?v=qqp6QN20CpE
# https://www.boot.dev/ con il codice TECHWITHTIM per 25% sconto

# Dunder (double underscore) or Magic Methods
# Ogni cosa che creo in python è un oggetto istanziato da una classe

str1 = "Hello"
str2 = "World"

print(str1+str2) # Possibile perchè ha implementato un Dunder
print(str1.__add__(str2))
print(str1.__len__())

################################OPERAZIONI ALGEBRICHE
class InventoryItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):      # Stringa per umani
        return f"L'oggetto {self.name} contiene {self.quantity} items"
    
    def __repr__(self):     # Stringa per developer
        return f"InventoryItem( name: {self.name}, quantity: {self.quantity} )"
    
    #Operatori aritmetici
    def __add__(self, other):       
        if isinstance(other, InventoryItem) and self.name == other.name:
            return InventoryItem(self.name, self.quantity + other.quantity)
        raise ValueError("Non posso sommare diversi InventoryItems")
    
    def __sub__(self, other):       
        if isinstance(other, InventoryItem) and self.name == other.name:
            return InventoryItem(self.name, self.quantity - other.quantity)
        raise ValueError("Non posso sommare diversi InventoryItems")
    
    def __mul__(self, factor):
        if isinstance(factor, (int, float)):
            return InventoryItem(self.name, int(self.quantity * factor))
        raise ValueError("Il moltiplicatore deve essere un numero!")
    
    def __truediv__(self, factor):
        if isinstance(factor, (int, float)) and factor != 0:
            return InventoryItem(self.name, int(self.quantity / factor))
        raise ValueError("Il moltiplicatore deve essere un numero!")
    
    #Comparisons
    def __eq__(self, other):        #Anche __ne__
        if isinstance(other, InventoryItem):
            return self.name == other.name and self.quantity == other.quantity
        raise ValueError("I due membri devono essere InventoryItem")
    
    def __gt__(self, other):  # Anche __gte__
        if isinstance(other, InventoryItem) and self.name == other.name:
            return self.quantity > other.quantity
        raise ValueError("I due membri devono essere InventoryItem")
    
    def __lt__(self, other):    # Anche __lte__
        if isinstance(other, InventoryItem) and self.name == other.name:
            self.quantity < other.quantity
        raise ValueError("I due membri devono essere InventoryItem")
    

item1 = InventoryItem("Apple", 10)
item2 = InventoryItem("Apple", 30)
item3 = InventoryItem("Samsung", 20)

print(item1)
print(item1.__repr__())
print(item1 + item2)
try:
    print(item1+item3)
except ValueError:
    print("Non posso sommare item1 e item3")

###########################################LISTE
#Vediamo adesso alcune operazioni con le liste

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedinList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, value):
        """Add Node to the end of the list"""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values)
    
    def __len__(self):
        """Definisce il comporamento di len()"""
        return self.size
    
    def __getitem__(self, index):
        """Enambe indexing (obj[index])"""
        if index<0 or index>self.size:
            raise IndexError("Attenzione il numero deve essere compreso nella lunghezza della lista")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value
    
    def __setitem__(self, index, value):
        """Enambe item assignment (obj[index])"""
        if index<0 or index>self.size:
            raise IndexError("Attenzione il numero deve essere compreso nella lunghezza della lista")
        current = self.head
        for _ in range(index):
            current = current.next
        current.value = value 
    
    def __delitem__(self, index):
        """Enambe item deletion  (obj[index])"""
        if index<0 or index>self.size:
            raise IndexError("Attenzione il numero deve essere compreso nella lunghezza della lista")
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index-1):
                current = current.next
            current.next = current.next.next
        self.size -= 1

    def __contains__(self, value):  # funziona con in
        """Definisce il comporamento di 'in'"""
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False 

ll = LinkedinList()
ll.append(10)
ll.append(20)
ll.append(30)
print(f"Lunghezza: {len(ll)}")
print(f"Primo oggetto: {ll[1]}")
ll[1]=25
print(f"Primo oggetto: {ll[1]}")
print(ll)
print(30 in ll)


################################CONTESTI
#Vediamo adesso come si comporta nei contesti
#Esiste se la classe ha __enter__ e __exit__

class DatabaseConnection:
    """Simula la connessione ad un db"""
    def __init__(self,db_name):
        self.db_bame = db_name
        self.connected = False
    
    def __enter__(self):
        self.connected = True
        print(f"Connected database '{self.db_bame}'")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.connected = False
        print(f"Disconnected database '{self.db_bame}'")
        if exc_type:
            print(f"An exception occurred {exc_value}")
        return True
    


with DatabaseConnection("ExampleDB") as db:
    print(f"Is connected? {db.connected}")


###############################ITERATORI

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > 0:
            value = self.current
            self.current -= 1
            return value
        else:
            raise StopIteration


for number in Countdown(5):
    print(number)