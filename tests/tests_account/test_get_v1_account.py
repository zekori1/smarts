from dm_api_account.apis.account.account_api import AccountApi
from dm_api_account.apis.login.login_api import LoginApi
from dm_api_account.models.login.post_v1_account_login_request_model import LoginCredentialsRequestModel
import structlog

import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False),
    ]
)


def test_post_v1_account_login():
    account = AccountApi()
    login = LoginApi()
    response = login.post_v1_account_login(
        json_data=LoginCredentialsRequestModel(
            login='test_user_9',
            password='test_user_9',

        )
    )
    token = response.headers['X-Dm-Auth-Token']
    response = account.get_v1_account(
        x_dm_auth_token=token
    )
    print(response)

    # account_login = LoginApi()
    # response = account_login.post_v1_account_login(
    #     login='test_user_5',
    #     password='test_user_5',
    #     remember_me=True
    #
    # )
    # # assert response.status_code == 200
    # x_dm = response.headers.get('X-Dm-Auth-Token')
    # print(x_dm)
    # assert response.status_code == 200

# def test_get_v1_account():
#     get_account = AccountApi()
#     response = get_account.get_v1_account(
#         x_dm_auth_token= x_dm,
#     )
#     print(response)
#     assert response.status_code == 200
