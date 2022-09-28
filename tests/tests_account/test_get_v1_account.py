from dm_api_account.models.login.post_v1_account_login_request_model import LoginCredentialsRequestModel

import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False),
    ]
)


def test_post_v1_account_login(account_api, login_api):
    response = login_api.post_v1_account_login(
        json_data=LoginCredentialsRequestModel(
            login='test_user_9',
            password='test_user_9',

        )
    )
    token = response.headers['X-Dm-Auth-Token']
    response = account_api.get_v1_account(
        x_dm_auth_token=token
    )
    print(response)


