import apis.dm_api_account.apis


class DmApiAccount:
    def __init__(self, host, headers=None):
        self.host = host
        self.headers = headers
        self.account_api = apis.dm_api_account.apis.AccountApi(self.host, self.headers)
        self.login_api = apis.dm_api_account.apis.LoginApi(self.host, self.headers)
