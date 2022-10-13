from apis.dm_api_account.models.login.post_v1_account_login_request_model import LoginCredentialsRequestModel

import pytest

import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False),
    ]
)


@pytest.mark.parametrize('login, password', [('test_user_10', 'test_user_10')])
def test_post_v1_account_login(dm_api_account, dm_db, login, password):
    response = dm_api_account.login_api.post_v1_account_login(
        json_data=LoginCredentialsRequestModel(
            login=login,
            password=password,

        )
    )
    token = response.headers['X-Dm-Auth-Token']
    response = dm_api_account.account_api.get_v1_account(
        x_dm_auth_token=token
    )
    print(response)
    rows = dm_db.get_user_by_login(login=login)
