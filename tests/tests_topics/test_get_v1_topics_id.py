import pytest
from apis.dm_api_account.models.login.post_v1_account_login_request_model import LoginCredentialsRequestModel
from urllib.parse import quote

decoder = lambda x: quote(x.encode('UTF-8'))


@pytest.mark.parametrize('login, password, remember_me', [('test_user_10', 'test_user_10', True)])
def test_get_v1_topics_id(dm_api_account, dm_api_forum, dm_db, login, password, remember_me):
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
    po = quote(forum_id)
    print(po)
    #
    response = dm_api_forum.forum_api.get_v1_fora_id_topics(forum_id=po)
    topics = response.json()['resources'][2]['id']
    print(topics)

    response = dm_api_forum.topic_api.get_v1_topics_id(
        x_dm_auth_token=x_dm,
        topics_id=topics
    )
    return response
