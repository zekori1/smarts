import pytest
from apis.dm_api_account.models.login.post_v1_account_login_request_model import LoginCredentialsRequestModel
from urllib.parse import quote
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False),
    ]
)

decoder = lambda x: quote(x.encode('UTF-8'))


@pytest.mark.parametrize('login, password, remember_me', [('test_user_10', 'test_user_10', True)])
def test_get_v1_fora(dm_api_account, dm_api_forum, dm_db, login, password, remember_me):
    response = dm_api_account.login_api.post_v1_account_login(
        json_data=LoginCredentialsRequestModel(
            login=login,
            password=password,
            remember_me=remember_me
        )
    )
    x_dm = response.headers.get('X-Dm-Auth-Token')
    print(x_dm)

    response = dm_api_forum.forum_api.get_v1_fora(
        x_dm_auth_token=x_dm
    )
    forum_id = response.json()['resources'][0]["id"]
    print(decoder(forum_id))

    # get_fora_id = ForumApi()
    response = dm_api_forum.forum_api.get_v1_fora_id(forum_id)
    assert response.status_code == 200
