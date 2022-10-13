from apis.dm_api_account import LoginCredentialsRequestModel


def test_post_v1_account_login(dm_api_account):
    response = dm_api_account.login_api.post_v1_account_login(
        json_data=LoginCredentialsRequestModel(
            login='test_user_9',
            password='test_user_9',
            remember_me=True
        )
    )
    # assert response.status_code == 200
    x_dm = response.headers.get('X-Dm-Auth-Token')
    print(x_dm)

    # def test_delete_v1_account_login():
    response = dm_api_account.login_api.delete_v1_account_login(
        x_dm_auth_token=x_dm
    )
    assert response.status_code == 204
