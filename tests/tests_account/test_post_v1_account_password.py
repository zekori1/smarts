from dm_api_account.models.login.post_v1_account_login_request_model import LoginCredentialsRequestModel
from dm_api_account.models.account.post_v1_account_password_request_model import ResetPasswordResponseModel


def test_post_v1_account_login(login_api, account_api):
    response = login_api.post_v1_account_login(
        json_data=LoginCredentialsRequestModel(
            login='test_user_5',
            password='test_user_5',
            remember_me=True
        )
    )
    x_dm = response.headers.get('X-Dm-Auth-Token')
    print(x_dm)
    assert response.status_code == 200
    response = account_api.post_v1_account_password(
        x_dm_auth_token=x_dm,
        json_data=ResetPasswordResponseModel(
            login='test_user_5',
            email='test_user_5@mail.ru'
        )
    )
    assert response.status_code == 200
