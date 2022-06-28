from HW17.base_api import BaseAPI


class AccountApi(BaseAPI):

    def __init__(self):
        super().__init__()
        self.account_url = "/Account/v1"
        self.generate_token_url = "/GenerateToken"
        self.authorized_url = "/Authorized"
        self.user_url = "/User"

    def post_user(self, headers=None, json=None):
        return self.post(url=f"{self.account_url}{self.user_url}", json=json, headers=headers)
