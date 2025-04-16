from django.conf import settings
import requests

class AuthorizeNet:
    def __init__(self):
        self.api_login_id = settings.AUTHORIZE_NET_API_LOGIN_ID
        self.transaction_key = settings.AUTHORIZE_NET_TRANSACTION_KEY
        self.endpoint = "https://api.authorize.net/xml/v1/request.api"

    def create_transaction(self, amount, card_number, expiration_date, card_code):
        transaction_request = {
            "createTransactionRequest": {
                "merchantAuthentication": {
                    "name": self.api_login_id,
                    "transactionKey": self.transaction_key
                },
                "transactionRequest": {
                    "transactionType": "authCaptureTransaction",
                    "amount": amount,
                    "payment": {
                        "creditCard": {
                            "cardNumber": card_number,
                            "expirationDate": expiration_date,
                            "cardCode": card_code
                        }
                    }
                }
            }
        }

        response = requests.post(self.endpoint, json=transaction_request)
        return response.json()

    def get_transaction_details(self, transaction_id):
        transaction_request = {
            "getTransactionDetailsRequest": {
                "merchantAuthentication": {
                    "name": self.api_login_id,
                    "transactionKey": self.transaction_key
                },
                "transactionId": transaction_id
            }
        }

        response = requests.post(self.endpoint, json=transaction_request)
        return response.json()