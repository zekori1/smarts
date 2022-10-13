import pytest
from apis.dm_api_account.models.login.post_v1_account_login_request_model import LoginCredentialsRequestModel
from apis.dm_api_forum.models.topics.post_v1_fora_id_topics import TopicsRequestModel
from apis.dm_api_forum.models.topics.post_v1_fora_id_topics import User
from apis.dm_api_forum.models.topics.post_v1_fora_id_topics import Rating
from apis.dm_api_forum.models.topics.post_v1_fora_id_topics import LastTopicComment
from apis.dm_api_forum.models.topics.post_v1_fora_id_topics import Forum
from datetime import datetime

from urllib.parse import quote

decoder = lambda x: quote(x.encode('UTF-8'))


@pytest.mark.parametrize('login, password, remember_me', [('test_user_10', 'test_user_10', True)])
def test_post_v1_fora_id(dm_api_account, dm_api_forum, dm_db, login, password, remember_me):
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

    author = User(
        login='test_user_10',
    )
    response = dm_api_forum.forum_api.post_v1_fora_id_topics(
        forum_id=po,
        x_dm_auth_token=x_dm,
        json_data=TopicsRequestModel(
            id=topics,
            author=author,
            title='Создаю тему через ручку, пипец я умный',
            description='Эта ручка создана по обрузу и подобию той, что я создавал через свагер',
        ))
    assert response.status_code == 201

    # rating = Rating(
    #     enabled=True,
    #     quality=0,
    #     quantity=0
    # )
    # author = User(
    #     login='test_user_10',
    #     roles='Guest',
    #     medium_picture_url='',
    #     small_picture_url='',
    #     status='',
    #     rating=rating
    # )
    # forum = Forum(
    #     id='Общий',
    #     unreadTopicsCount=0
    # )
    # user1 = User(
    #     login='test_user_10',
    #     roles='Guest',
    #     medium_picture_url='',
    #     small_picture_url='',
    #     status='',
    #     rating=rating,
    #     online='',
    #     name='',
    #     location='',
    #     registration=datetime.now()
    # )
    # user2 = User(
    #     login='',
    #     roles='',
    #     medium_picture_url='',
    #     small_picture_url='',
    #     status='',
    #     rating=rating,
    #     online='',
    #     name='',
    #     location='',
    #     registration=str(datetime.now())
    # )
    # last_comment = LastTopicComment(
    #     created='',
    #     author=user1,
    #     commentsCount=0,
    #     unreadCommentsCount=0,
    #     forum=forum,
    #     likes=user2
    # )
    #
    # response = dm_api_forum.forum_api.post_v1_fora_id_topics(
    #     forum_id=po,
    #     x_dm_auth_token=x_dm,
    #     json_data=TopicsRequestModel(
    #         id=topics,
    #         author=author,
    #         online='',
    #         name='',
    #         location='',
    #         registration=datetime.now(),
    #         created='',
    #         title='Создаю тему через ручку, пипец я умный',
    #         description='Эта ручка создана по обрузу и подобию той, что я создавал через свагер',
    #         attached=True,
    #         closed=True,
    #         lastComment=last_comment
    #     ))
    # return response
