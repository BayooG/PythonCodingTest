import random

def PremiumPaymentGateway(payment):
    return bool(random.getrandbits(1))

def ExpensivePaymentGateway(payment):
    return bool(random.getrandbits(1))
def CheapPaymentGateway(payment):
    return bool(random.getrandbits(1))