from dm_api_account.apis.account.account_api import AccountApi
from dm_api_account.apis.login.login_api import LoginApi
from dm_api_account.models.login.post_v1_account_login_request_model import LoginCredentialsRequestModel
from dm_api_account.models.account.put_v1_account_email_request_model import ChangeEmailResponseModel


def test_post_v1_account_login():
    account_login = LoginApi()
    response = account_login.post_v1_account_login(
        json_data=LoginCredentialsRequestModel(
            login='test_user_5',
            password='test_user_5',
            remember_me=True
        )
    )
    # assert response.status_code == 200
    x_dm = response.headers.get('X-Dm-Auth-Token')
    print(x_dm)

    # def test_put_v1_account_email():
    account_email = AccountApi()
    response = account_email.put_v1_account_email(
        x_dm_auth_token=x_dm,
        json_data=ChangeEmailResponseModel(
            login='test_user_8',
            password='test_user_88',
            email='test_user_8@mail.ru',
        )
    )
    print(response)
    assert response.status_code == 200
