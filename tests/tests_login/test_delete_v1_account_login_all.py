import pytest
from apis.dm_api_account import LoginCredentialsRequestModel


@pytest.mark.parametrize('login, password, remember_me', [('test_user_10', 'test_user_10', True)])
def test_post_v1_account_login(dm_api_account, dm_db, login, password, remember_me):
    response = dm_api_account.login_api.post_v1_account_login(
        json_data=LoginCredentialsRequestModel(
            login=login,
            password=password,
            remember_me=remember_me

        )
    )
    x_dm = response.headers.get('X-Dm-Auth-Token')
    print(x_dm)

    # def test_delete_v1_account_login_all():
    response = dm_api_account.login_api.delete_v1_account_login_all(
        x_dm_auth_token=x_dm
    )
    assert response.status_code == 204
