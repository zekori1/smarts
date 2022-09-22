from dm_api_account.apis.login.login_api import LoginApi
from dm_api_account.models.login.post_v1_account_login_request_model import LoginCredentialsRequestModel


def test_post_v1_account_login():
    account_login = LoginApi()
    response = account_login.post_v1_account_login(
        json_data=LoginCredentialsRequestModel(
            login='test_user_9',
            password='test_user_9',
            remember_me=True
        )
    )
    # assert response.status_code == 200
    x_dm = response.headers.get('X-Dm-Auth-Token')
    print(x_dm)



