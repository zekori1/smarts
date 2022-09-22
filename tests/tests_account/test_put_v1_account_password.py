from dm_api_account.apis.account.account_api import AccountApi
from dm_api_account.apis.login.login_api import LoginApi
from helpers.mailhog.mailhog_client import MailHogClient
from dm_api_account.models.login.post_v1_account_login_request_model import LoginCredentialsRequestModel
from dm_api_account.models.account.put_v1_account_password_request_model import ChangePasswordResponseModel


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
    assert response.status_code == 200
    # def test_post_v1_account_password():
    post_account_password = AccountApi()
    mailhog = MailHogClient()
    activation_token = mailhog.get_token()
    response = post_account_password.put_v1_account_password(
        x_dm_auth_token=x_dm,
        json_data=ChangePasswordResponseModel(
            login='test_user_8',
            token=activation_token,
            oldpassword='test_user_8',
            newpassword='test_user_88'
        )
    )
    assert response.status_code == 200
