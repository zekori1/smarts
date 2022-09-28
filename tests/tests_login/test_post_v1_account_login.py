from dm_api_account.models.login.post_v1_account_login_request_model import LoginCredentialsRequestModel


def test_post_v1_account_login(login_api):
    response = login_api.post_v1_account_login(
        json_data=LoginCredentialsRequestModel(
            login='test_user_9',
            password='test_user_9',
            remember_me=True
        )
    )
    x_dm = response.headers.get('X-Dm-Auth-Token')
    print(x_dm)
