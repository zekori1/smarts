from dm_api_account.models.login.post_v1_account_login_request_model import LoginCredentialsRequestModel


def test_post_v1_account_login(login_api):
    response = login_api.post_v1_account_login(
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
    response = login_api.delete_v1_account_login(
        x_dm_auth_token=x_dm
    )
    assert response.status_code == 204
