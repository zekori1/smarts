from dm_api_account.apis import *


class DmApiAccount:
    def __init__(self, host, headers=None):
        self.host = host
        self.headers = headers
        self.account_api = AccountApi(self.host, self.headers)
        self.login_api = LoginApi(self.host, self.headers)
