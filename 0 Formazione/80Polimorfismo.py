#Vediamo come funziona il polimorfismo

from abc import ABC, abstractclassmethod

# questa classe è astratta
# ciò significa che ogni classe che deriva da questa deve implemetare i metodi in essa definiti.
# Per forza
class PaymentType(ABC):
    payNumber: int = 0                  # Questa variabile è di classe e può essere richiamata solo come PaymentType.payNumber

    @abstractclassmethod                # Per ogni metodo che si vuole creare, bisogna mettere questo placeholder
    def process_payment(self, amount: float) -> None:
        ...

class CreditCard(PaymentType):
    def process_payment(self, amount: float) -> None:
        PaymentType.payNumber += 1
        print(f'Processato pagamento carta €{amount}')

class Cash(PaymentType):
    def process_payment(self, amount: float) -> None:
        PaymentType.payNumber += 1
        print(f'Processato pagamento cash €{amount}')

class Satispay(PaymentType):
    def process_payment(self, amount: float) -> None:
        PaymentType.payNumber += 1
        print(f'Processato pagamento satispay €{amount}')

def cashout(paymentType: PaymentType, amt: float) -> None:
    paymentType.process_payment(amt)

credit_card : CreditCard = CreditCard()
cash : Cash = Cash()
satispay: Satispay = Satispay()

cashout(credit_card,100)
cashout(cash,1000)
cashout(satispay,200)

print(f'Ci sono {PaymentType.payNumber} tipi di pagamento istanziati')