import pytest
from apis.dm_api_account import LoginCredentialsRequestModel
from apis.dm_api_account.models.account.post_v1_account_password_request_model import ResetPasswordResponseModel


@pytest.mark.parametrize('login, password, email, remember_me',
                         [('test_user_10', 'test_user_10', 'test_user_10@mail.ru', True)])
def test_post_v1_account_login(dm_api_account, dm_db, login, password, remember_me, email):
    response = dm_api_account.login_api.post_v1_account_login(
        json_data=LoginCredentialsRequestModel(
            login=login,
            password=password,
            remember_me=remember_me
        )
    )
    x_dm = response.headers.get('X-Dm-Auth-Token')
    print(x_dm)
    assert response.status_code == 200
    response = dm_api_account.account_api.post_v1_account_password(
        x_dm_auth_token=x_dm,
        json_data=ResetPasswordResponseModel(
            login=login,
            email=email
        )
    )
    assert response.status_code == 200
    rows = dm_db.get_user_by_login(login=login)
