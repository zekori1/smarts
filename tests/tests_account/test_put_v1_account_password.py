import pytest
from apis.dm_api_account.models.login.post_v1_account_login_request_model import LoginCredentialsRequestModel
from apis.dm_api_account.models.account.put_v1_account_password_request_model import ChangePasswordResponseModel


@pytest.mark.parametrize('login, password, email, remember_me, new_password',
                         [('test_user_10', 'test_user_10', 'test_user_10@mail.ru', True, 'test_user_xui')])
def test_post_v1_account_login(dm_api_account, mailhog, dm_db, login, password, remember_me, email, new_password):
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
    # def test_post_v1_account_password():
    activation_token = mailhog.get_token()
    response = dm_api_account.account_api.put_v1_account_password(
        x_dm_auth_token=x_dm,
        json_data=ChangePasswordResponseModel(
            login=login,
            token=activation_token,
            old_password=password,
            new_password=new_password
        )
    )
    assert response.status_code == 200
    rows = dm_db.get_user_by_login(login=login)
