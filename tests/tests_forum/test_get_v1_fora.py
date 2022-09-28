from dm_api_account.models.login.post_v1_account_login_request_model import LoginCredentialsRequestModel
from urllib.parse import quote, unquote

decoder = lambda x: quote(x.encode('UTF-8'))


def test_get_v1_fora(login_api, forum_api):
    response = login_api.post_v1_account_login(
        json_data=LoginCredentialsRequestModel(
            login='test_user_7',
            password='test_user_7',
            remember_me=True
        )
    )
    x_dm = response.headers.get('X-Dm-Auth-Token')
    print(x_dm)

    response = forum_api.get_v1_fora(
        x_dm_auth_token=x_dm
    )
    id = response.json()['resources'][0]["id"]
    print(decoder(id))
    # assert response.status_code == 200
