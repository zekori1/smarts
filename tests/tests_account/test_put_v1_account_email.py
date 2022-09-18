from dm_api_account.apis.account import AccountApi
from dm_api_account.apis.login import LoginApi


def test_post_v1_account_login():
    account_login = LoginApi()
    response = account_login.post_v1_account_login(
        login='test_user_8',
        password='test_user_88',
        remember_me=True

    )
    # assert response.status_code == 200
    x_dm = response.headers.get('X-Dm-Auth-Token')
    print(x_dm)

    # def test_put_v1_account_email():
    account_email = AccountApi()
    response = account_email.put_v1_account_email(
        login='test_user_8',
        password='test_user_88',
        email='test_user_8@mail.ru',
        x_dm_auth_token=x_dm
    )
    print(response)
    assert response.status_code == 200
