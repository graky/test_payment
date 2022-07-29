from aiohttp import TCPConnector, BasicAuth
from settings import LOGIN, PASSWORD, SERVICE
from abstract_client import AbstractInteractionClient
from models import interaction_method_schema_dict


class CloudPaymentsClient(AbstractInteractionClient):
    CONNECTOR = TCPConnector()
    BASE_URL = "https://api.cloudpayments.ru/"
    SERVICE = SERVICE

    def __init__(self, login: str = LOGIN, password: str = PASSWORD):
        super().__init__()
        self.auth = BasicAuth(login=login, password=password)

    async def charge(self, interaction_method, **kwargs):
        json_data = interaction_method_schema_dict.get(interaction_method)().dump(
            kwargs
        )
        charge_url = self.endpoint_url("cards/charge")
        response = await self.post(
            interaction_method, charge_url, auth=self.auth, json=json_data
        )
        await self.close()
        return response
