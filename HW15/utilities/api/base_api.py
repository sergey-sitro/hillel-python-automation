import requests
from HW15.utilities.run_settings import ReadConfig


class BaseAPI:

    def __init__(self):
        self.base_url = ReadConfig.get_api_url()
        self.request = requests

    def get(self, url, body=None, headers=None, params=None):
        response = self.request.get(f"{self.base_url}{url}", data=body, headers=headers, params=params)
        return response

    def post(self, url, json=None, headers=None, params=None):
        response = self.request.post(f"{self.base_url}{url}", json=json, headers=headers, params=params)
        return response

    def delete(self, url, json=None, headers=None, params=None):
        response = self.request.delete(f"{self.base_url}{url}", json=json, headers=headers, params=params)
        return response
