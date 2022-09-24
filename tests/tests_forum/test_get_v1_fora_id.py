from dm_api_forum.apis.forum_api import ForumApi
from dm_api_account.apis.login.login_api import LoginApi
from dm_api_account.models.login.post_v1_account_login_request_model import LoginCredentialsRequestModel

def test_get_v1_fora():
    account_login = LoginApi()
    response = account_login.post_v1_account_login(
        json_data=LoginCredentialsRequestModel(
            login='test_user_7',
            password='test_user_7',
            remember_me=True
        )
    )
    x_dm = response.headers.get('X-Dm-Auth-Token')
    print(x_dm)

    get_fora_id = ForumApi()
    response = get_fora_id.get_v1_fora_id()