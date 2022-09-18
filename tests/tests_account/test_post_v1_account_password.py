from dm_api_account.apis.account import AccountApi
from dm_api_account.apis.login import LoginApi

def test_post_v1_account_login():
    account_login = LoginApi()
    response = account_login.post_v1_account_login(
        login='test_user_5',
        password='test_user_5',
        remember_me=True

    )
    # assert response.status_code == 200
    x_dm = response.headers.get('X-Dm-Auth-Token')
    print(x_dm)
    assert response.status_code == 200
# def test_post_v1_account_password():
    post_account_password = AccountApi()
    response = post_account_password.post_v1_account_password(
        login='test_user_5',
        email='test_user_5@mail.ru',
        x_dm_auth_token=x_dm
    )
    assert response.status_code == 200