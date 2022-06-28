from HW17.config import config
import requests


class BaseAPI:

    def __init__(self):
        self.base_url = config['base_url']
        self.request = requests

    def get(self, url, body=None, headers=None, params=None):
        response = self.request.get(f"{self.base_url}{url}", data=body, headers=headers, params=params)
        return response

    def post(self, url, body=None, headers=None, params=None):
        response = self.request.post(f"{self.base_url}{url}", data=body, headers=headers, params=params)
        return response
