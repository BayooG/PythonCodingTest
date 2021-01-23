from .services import CheapPaymentGateway, ExpensivePaymentGateway, PremiumPaymentGateway

def ProcessPayment(payment):
    status = False
    
    if payment['Amount'] <= 20:
        status = CheapPaymentGateway(payment)
    elif 21 <= payment['Amount'] < 500 :
        status = ExpensivePaymentGateway(payment)
        if not status:
           status = CheapPaymentGateway(payment) 
    else:
        for _ in range(3):
            status = PremiumPaymentGateway(payment)
            if status: 
                break
    if status:
        return True
    else:
        raise Exception('Payment could not be processd')
    