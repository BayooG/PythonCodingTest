import datetime as dt
def validate_payment(data):
    """check if the given rules are applied on the posted payment (request) 

    :param data: payment
    :type data: flask_restx api.model
    :return: payment validation 
    :rtype: bool
    """
    if all([data.get('ExpirationDate'), data.get('CreditCardNumber'), data.get('Amount')]):  
        Expiration_date = dt.datetime.fromisoformat(data['ExpirationDate'][:-1])
        if Expiration_date > dt.datetime.now():
            if validate_cc_number(data['CreditCardNumber']):
                if data['Amount'] > 0:
                    security_code = data.get('SecurityCode', None)
                    if security_code is not None:
                        if len(security_code) == 3:
                            return True
                    else:
                        return True
            
    return False


def validate_cc_number(cc_num):
    """checks the given number is a valid credit card number

    :param cc_num: credit card number
    :type cc_num: str
    :return: credit card validation
    :rtype: bool
    """
    try:
        # reverse the credit card number
        cc_num = cc_num[::-1].replace(' ','')
        # convert to integer list
        cc_num = [int(x) for x in cc_num]
        # double every second digit
        doubled_second_digit_list = list()
        digits = list(enumerate(cc_num, start=1))
        for index, digit in digits:
            if index % 2 == 0:
                doubled_second_digit_list.append(digit * 2)
            else:
                doubled_second_digit_list.append(digit)

        # add the digits if any number is more than 9
        doubled_second_digit_list = [sum_digits(x) for x in doubled_second_digit_list]
        # sum all digits
        sum_of_digits = sum(doubled_second_digit_list)
        # return True or False
        return sum_of_digits % 10 == 0
    except:
        return False

def sum_digits(digit):
    if digit < 10:
        return digit
    else:
        sum = (digit % 10) + (digit // 10)
        return sum