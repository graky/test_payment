from marshmallow import Schema, fields, validate


currency_codes = [
    "RUB",
    "EUR",
    "USD",
    "GBP",
    "UAH",
    "BYR",
    "BYN",
    "KZT",
    "AZN",
    "CHF",
    "CZK",
    "CAD",
    "PLN",
    "SEK",
    "TRY",
    "CNY",
    "INR",
    "BRL",
    "ZAR",
    "UZS",
    "BGN",
    "RON",
    "AUD",
    "HKD",
    "GEL",
    "KGS",
    "AMD",
    "AED",
]

culture_codes = ["ru-RU", "en-US", "lv", "az", "kk", "uk", "pl", "vi", "tr"]


class ChargeCryptogramPaySchema(Schema):
    Amount = fields.Float(required=True)
    Currency = fields.Str(validate=validate.OneOf(currency_codes))
    IpAddress = fields.Str()
    CardCryptogramPacket = fields.Str(required=True)
    Name = fields.Str()
    PaymentURL = fields.Str()
    InvoiceId = fields.Str()
    Description = fields.Str()
    CultureName = fields.Str(validate=validate.OneOf(culture_codes))
    AccountId = fields.Str()
    Email = fields.Str()
    Payer = fields.Dict()
    JsonData = fields.Dict(
        keys=fields.Str(),
        values=fields.Str(),
        required=False,
        data_key="JsonData",
    )


interaction_method_schema_dict = {"charge_cryptogram_pay": ChargeCryptogramPaySchema}
