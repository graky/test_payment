Клиент - класс CloudPaymentsClient, наследуемый от AbstractInteractionClient. 

Оплата charge с криптограммой осуществляется методом charge, класса CloudPaymentsClient с параметром interaction_method=charge_cryptogram_pay.
Параметры запроса задаются остальными аргументами в соответствии с https://developers.cloudpayments.ru/#oplata-po-kriptogramme

Тестирование осуществляется командой python -m unittest test.tests