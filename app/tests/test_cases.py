from app.manage import application


def test_0():
    """
        valid test case
        missing optional field `SecurityCode`
    """
    url = '/api/v1/payment'
    client = application.test_client()
    body = {
        "CreditCardNumber": "4111 1111 1111 1111",
        "CardHolder": "obay daba",
        "ExpirationDate": "2022-06-23T19:25:21.356Z",
        "SecurityCode": "777",
        "Amount": 312.20
    }
    response = client.post(url, json=body)
    print(response)
    
    assert response.status_code == 200

def test_1():
    """
    valid test case
    """
    url = '/api/v1/payment'
    client = application.test_client()
    body = {
        "CreditCardNumber": "4111 1111 1111 1111",
        "CardHolder": "obay daba",
        "ExpirationDate": "2021-06-23T19:25:21.356Z",
        "SecurityCode": "777",
        "Amount": 312.20
    }
    response = client.post(url, json=body)
    print(response)
    
    assert response.status_code == 200
    
def test_2():
    """
    invalid test case
    datetime in the past
    """
    url = '/api/v1/payment'
    client = application.test_client()
    body = {
        "CreditCardNumber": "4111 1111 1111 1111",
        "CardHolder": "obay daba",
        "ExpirationDate": "2012-06-23T19:25:21.356Z",
        "SecurityCode": "777",
        "Amount": 312.20
    }
    response = client.post(url, json=body)
    print(response)
    
    assert response.status_code == 400

def test_3():
    """
        invalid test case
        invalid credit card number
    """
    url = '/api/v1/payment'
    client = application.test_client()
    body = {
        "CreditCardNumber": "4171 1111 1111 1111",
        "CardHolder": "obay daba",
        "ExpirationDate": "2022-06-23T19:25:21.356Z",
        "SecurityCode": "777",
        "Amount": 312.20
    }
    response = client.post(url, json=body)
    print(response)
    
    assert response.status_code == 400
    
def test_4():
    """
        invalid test case
        missing `CreditCardNumber`
    """
    url = '/api/v1/payment'
    client = application.test_client()
    body = {
        "CardHolder": "obay daba",
        "ExpirationDate": "2022-06-23T19:25:21.356Z",
        "SecurityCode": "777",
        "Amount": 312.20
    }
    response = client.post(url, json=body)
    print(response)
    
    assert response.status_code == 400
    
def test_5():
    """
        invalid test case
        wrong `SecurityCode`
    """
    url = '/api/v1/payment'
    client = application.test_client()
    body = {
        "CreditCardNumber": "4111 1111 1111 1111",
        "CardHolder": "obay daba",
        "ExpirationDate": "2022-06-23T19:25:21.356Z",
        "SecurityCode": "7277",
        "Amount": 312.20
    }
    response = client.post(url, json=body)
    print(response)
    
    assert response.status_code == 400

def test_6():
    """
        invalid test case
        negative `Amount`
    """
    url = '/api/v1/payment'
    client = application.test_client()
    body = {
        "CreditCardNumber": "4111 1111 1111 1111",
        "CardHolder": "obay daba",
        "ExpirationDate": "2022-06-23T19:25:21.356Z",
        "SecurityCode": "727",
        "Amount": -312.20
    }
    response = client.post(url, json=body)
    print(response)
    
    assert response.status_code == 400
    
def test_7():
    """
        invalid test case
        zero `Amount`
    """
    url = '/api/v1/payment'
    client = application.test_client()
    body = {
        "CreditCardNumber": "4111 1111 1111 1111",
        "CardHolder": "obay daba",
        "ExpirationDate": "2022-06-23T19:25:21.356Z",
        "SecurityCode": "727",
        "Amount": 0
    }
    response = client.post(url, json=body)
    print(response)
    
    assert response.status_code == 400