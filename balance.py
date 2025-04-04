import random

def balance():
    salary = float(input("Please tell me your salary🤑: "))
    balance = salary*random.uniform(0.1, 0.9)
    balance = round(balance,2)
    return balance
