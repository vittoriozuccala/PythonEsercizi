def add_numbers(*args):
    return sum(args)

def show_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    
    print('age' in list(kwargs.keys()))
    
    if any(s in 'age' for s in kwargs):
        print("Presente")
    else:
        print("Non presente")

print(add_numbers(1, 2, 3, 4))  # Outputs: 10
show_details(name="Alice", age=25, tipo = "solido")  # Outputs: name: Alice, age: 25


def order_pizza(size: str, *toppings, **details):
    print(f"Il cliente vuole una pizza {size} con i seguenti ingredienti:")
    for topping in toppings:
        print(f"- {topping}")
    print("ed i seguenti dettagli: ")
    for key, value in details.items():
        print(f"- {key}: {value}")


order_pizza("large", "pepperoni", "cipolla", "gorgonzola", delivery = "in casa", tempo = "veloce")
