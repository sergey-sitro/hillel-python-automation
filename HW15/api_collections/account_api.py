import allure
from HW15.utilities.api.base_api import BaseAPI


class AccountApi(BaseAPI):

    def __init__(self):
        super().__init__()
        self.account_url = "/Account/v1"
        self.generate_token_url = "/GenerateToken"
        self.authorized_url = "/Authorized"
        self.user_url = "/User"

    @allure.step
    def post_user(self, headers=None, json=None):
        return self.post(url=f"{self.account_url}{self.user_url}", json=json, headers=headers)

    @allure.step
    def post_generate_token(self, headers=None, json=None):
        return self.post(url=f"{self.account_url}{self.generate_token_url}", json=json, headers=headers)

    @allure.step
    def post_authorized(self, headers=None, json=None):
        return self.post(url=f"{self.account_url}{self.authorized_url}", json=json, headers=headers)

    @allure.step
    def get_user(self, uuid=None, headers=None):
        return self.get(url=f"{self.account_url}{self.user_url}/{uuid}", headers=headers)

    @allure.step
    def delete_user(self, uuid=None, headers=None):
        return self.delete(url=f"{self.account_url}{self.user_url}/{uuid}", headers=headers)
