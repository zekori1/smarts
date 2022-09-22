from dm_api_account.apis.account.account_api import AccountApi
from dm_api_account.apis.login.login_api import LoginApi
from dm_api_account.models.login.post_v1_account_login_request_model import LoginCredentialsRequestModel
from dm_api_account.models.account.post_v1_account_password_request_model import ResetPasswordResponseModel


def test_post_v1_account_login():
    account_login = LoginApi()
    response = account_login.post_v1_account_login(
        json_data=LoginCredentialsRequestModel(
            login='test_user_5',
            password='test_user_5',
            remember_me=True
        )
    )
    x_dm = response.headers.get('X-Dm-Auth-Token')
    print(x_dm)
    assert response.status_code == 200
    # def test_post_v1_account_password():
    post_account_password = AccountApi()
    response = post_account_password.post_v1_account_password(
        x_dm_auth_token=x_dm,
        json_data=ResetPasswordResponseModel(
            login='test_user_5',
            email='test_user_5@mail.ru'
        )
    )
    assert response.status_code == 200
