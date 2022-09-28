from urllib.parse import quote, unquote
from dm_api_account.models.login.post_v1_account_login_request_model import LoginCredentialsRequestModel
import structlog

decoder = lambda x: quote(x.encode('UTF-8'))
undecoder = lambda x: unquote(x.encode('UTF-8'))

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False),
    ]
)


def test_get_v1_fora_id_topics(dm_api_account, dm_api_forum):
    response = dm_api_account.login_api.post_v1_account_login(
        json_data=LoginCredentialsRequestModel(
            login='test_user_9',
            password='test_user_9',
            remember_me=True
        )
    )
    x_dm = response.headers.get('X-Dm-Auth-Token')
    print(x_dm)

    response = dm_api_forum.forum_api.get_v1_fora(
        x_dm_auth_token=x_dm
    )

    forum_id = response.json()['resources'][0]["id"]
    po = quote(forum_id)
    print(po)

    response = dm_api_forum.forum_api.get_v1_fora_id_topics(forum_id=po)
    return response.json()
