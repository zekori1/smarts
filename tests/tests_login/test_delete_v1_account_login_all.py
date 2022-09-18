from dm_api_account.apis.login import LoginApi


def test_post_v1_account_login():
    account_login = LoginApi()
    response = account_login.post_v1_account_login(
        login='test_user_9',
        password='test_user_9',
        remember_me=True

    )
    # assert response.status_code == 200
    x_dm = response.headers.get('X-Dm-Auth-Token')
    print(x_dm)


# def test_delete_v1_account_login_all():
    delete_account_login_all=LoginApi()
    response = delete_account_login_all.delete_v1_account_login_all(
        x_dm_auth_token=x_dm
    )
    assert response.status_code == 204
