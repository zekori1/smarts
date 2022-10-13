from apis.dm_api_account.models.account.post_v1_account_request_model import RegistrationRequestModel
from apis.dm_api_account.models.account.get_v1_account_response_model import UserDetailsEnvelopeResponseModel
from apis.dm_api_account.models.account.post_v1_account_password_request_model import ResetPasswordResponseModel
from apis.dm_api_account.models.account.put_v1_account_email_request_model import ChangeEmailResponseModel
from apis.dm_api_account.models.account.put_v1_account_password_request_model import ChangePasswordResponseModel
from apis.dm_api_account.models.account.put_v1_account_token_request_model import UserEnvelopeResponseModel
from restclient.restclient import RestClient


class AccountApi:
    def __init__(self, host, headers=None):
        self.headers = headers
        self.host = host
        self.client = RestClient(host=self.host)
        if headers:
            self.client.headers = self

    def post_v1_account(self, json_data: RegistrationRequestModel):
        headers = {
            'accept': '*/*',

        }

        response = self.client.post(
            path=f'/v1/account',
            headers=headers,
            json=json_data.to_struct()
        )
        return response

    def get_v1_account(self, x_dm_auth_token) -> UserDetailsEnvelopeResponseModel:
        headers = {
            'accept': 'text/plain',
            'X-Dm-Auth-Token': x_dm_auth_token,
        }

        response = self.client.get(
            path=f'/v1/account',
            headers=headers
        )
        response_json = response.json()
        return UserDetailsEnvelopeResponseModel(**response_json)

    def put_v1_account_token(self, token: str) -> UserEnvelopeResponseModel:
        headers = {
            'accept': 'text/plain',
        }

        response = self.client.put(
            path=f'/v1/account/{token}',
            headers=headers

        )
        response_json = response.json()
        return UserEnvelopeResponseModel(**response_json)

    def post_v1_account_password(self, x_dm_auth_token, json_data: ResetPasswordResponseModel):
        headers = {
            'accept': 'text/plain',
            'X-Dm-Auth-Token': x_dm_auth_token,
            # Already added when you pass json= but not when you pass data=
            # 'Content-Type': 'application/json',
        }

        response = self.client.post(
            path=f'/v1/account/password',
            headers=headers,
            json=json_data.to_struct()
        )
        return response

    def put_v1_account_password(self, x_dm_auth_token, json_data: ChangePasswordResponseModel):
        headers = {
            'accept': 'text/plain',
            'X-Dm-Auth-Token': x_dm_auth_token,
            # Already added when you pass json= but not when you pass data=
            # 'Content-Type': 'application/json',
        }

        response = self.client.put(
            path=f'/v1/account/password',
            headers=headers,
            json=json_data.to_struct()
        )
        return response
        # один токен берем от авторизации другой от смены пароля на почте

    def put_v1_account_email(self, x_dm_auth_token, json_data: ChangeEmailResponseModel):
        headers = {
            'accept': 'text/plain',
            'X-Dm-Auth-Token': x_dm_auth_token,
            # Already added when you pass json= but not when you pass data=
            # 'Content-Type': 'application/json',
        }
        response = self.client.put(
            path=f'/v1/account/email',
            headers=headers,
            json=json_data.to_struct()
        )
        return response
