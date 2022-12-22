import errors 
import random
class Account():
    def __init__(self,balance,currency,acc_type,IBAN):
        cIBAn = "BG9812"
        if type(balance) != float:
            raise errors.InvalidDataFormat
        else:
            self.balance = balance
        if currency != "BGN" or currency !="EUR" or currency != "USD" or currency !="JPY":
            raise errors.InvalidDataFormat
        else:
            self.currency = currency
        if acc_type != "CURRENT" or acc_type !="SAVINGS" or acc_type != "CREDIT":
            raise errors.InvalidAccountType 
        else:
            self.acc_type = acc_type
        self.IBAN = cIBAn
        for i in range(10):
           current = random.randint(1,9)
           cIBAn += str(current)
    def print(self):
        print(f'{self.balance}/{self.currency}/{self.acc_type}/{self.IBAN}')
        
#НЕ РАБОТИ