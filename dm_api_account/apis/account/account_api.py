import requests
from dm_api_account.models.account.post_v1_account_request_model import RegistrationRequestModel
from dm_api_account.models.account.get_v1_account_response_model import UserDetailsEnvelopeResponseModel


class AccountApi:
    def __init__(self, host='http://localhost:5051'):
        self.host = host

    def post_v1_account(self, json_data: RegistrationRequestModel):
        headers = {
            'accept': '*/*',

        }

        response = requests.post(
            url=f'{self.host}/v1/account',
            headers=headers,
            json=json_data.to_struct()
        )
        return response

    def get_v1_account(self, x_dm_auth_token) -> UserDetailsEnvelopeResponseModel:
        headers = {
            'accept': 'text/plain',
            'X-Dm-Auth-Token': x_dm_auth_token,
        }

        response = requests.get(
            url=f'{self.host}/v1/account',
            headers=headers
        )
        response_json = response.json()
        return UserDetailsEnvelopeResponseModel(**response_json)

    def put_v1_account_token(self, token):
        headers = {
            'accept': 'text/plain',
        }

        response = requests.put(
            url=f'{self.host}/v1/account/{token}',
            headers=headers

        )
        return response

    def post_v1_account_password(self, login, email, x_dm_auth_token):
        headers = {
            'accept': 'text/plain',
            'X-Dm-Auth-Token': x_dm_auth_token,
            # Already added when you pass json= but not when you pass data=
            # 'Content-Type': 'application/json',
        }

        json_data = {
            'login': login,
            'email': email,
        }

        response = requests.post(
            url=f'{self.host}/v1/account/password',
            headers=headers,
            json=json_data
        )
        return response

    def put_v1_account_password(self, login, token, oldpassword, newpassword, x_dm_auth_token):
        headers = {
            'accept': 'text/plain',
            'X-Dm-Auth-Token': x_dm_auth_token,
            # Already added when you pass json= but not when you pass data=
            # 'Content-Type': 'application/json',
        }

        json_data = {
            'login': login,
            'token': token,
            'oldPassword': oldpassword,
            'newPassword': newpassword,
        }

        response = requests.put(
            url=f'{self.host}/v1/account/password',
            headers=headers,
            json=json_data)
        return response
        # один токен берем от авторизации другой от смены пароля на почте

    def put_v1_account_email(self, login, password, email, x_dm_auth_token):
        headers = {
            'accept': 'text/plain',
            'X-Dm-Auth-Token': x_dm_auth_token,
            # Already added when you pass json= but not when you pass data=
            # 'Content-Type': 'application/json',
        }

        json_data = {
            'login': login,
            'password': password,
            'email': email,
        }

        response = requests.put(
            url=f'{self.host}/v1/account/email',
            headers=headers,
            json=json_data
        )
        return response
