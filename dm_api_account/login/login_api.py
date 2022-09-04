import pprint
import json
import requests


class LoginApi:
    def __init__(self, host):
        self.host = host

    def post_v1_account_login(self, login, password, remember_me):
        headers = {
            'accept': 'text/plain',
        }

        json_data = {
            'login': login,
            'password': password,
            'rememberMe': remember_me,
        }

        response = requests.post(
            url=f'{self.host}/v1/account/login',
            headers=headers,
            json=json_data
        )
        return response

    def delete_v1_account_login(self, x_dm_auth_token):
        headers = {
            'accept': '*/*',
            'X-Dm-Auth-Token': x_dm_auth_token,
        }

        response = requests.delete(
            url=f'{self.host}/v1/account/login',
            headers=headers
        )
        return response


    def delete_v1_account_login_all(self, x_dm_auth_token):
        headers = {
            'accept': '*/*',
            'X-Dm-Auth-Token': x_dm_auth_token,
        }

        response = requests.delete(
            url=f'{self.host}/v1/account/login/all',
            headers=headers
        )
        return response
