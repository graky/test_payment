from unittest import IsolatedAsyncioTestCase
from client import CloudPaymentsClient


class ChargePayTest(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.kwargs = {
            "Amount": 10,
            "Currency": "RUB",
            "InvoiceId": "1234567",
            "IpAddress": "123.123.123.123",
            "Description": "Оплата товаров в example.com",
            "AccountId": "user_x",
            "Name": "CARDHOLDER NAME",
            "CardCryptogramPacket": "some_token",
            "Payer": {
                "FirstName": "Тест",
                "LastName": "Тестов",
                "MiddleName": "Тестович",
                "Birth": "1955-02-24",
                "Address": "тестовый проезд дом тест",
                "Street": "Lenina",
                "City": "MO",
                "Country": "RU",
                "Phone": "123",
                "Postcode": "345",
            },
        }

    async def test_charge_pay(self):

        pay = CloudPaymentsClient()
        response = await pay.charge(
            "charge_cryptogram_pay", **self.kwargs
        )
        self.assertIsNone(response.get("Message"))
        self.assertTrue(response.get("Success"))
