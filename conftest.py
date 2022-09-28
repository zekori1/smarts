import pytest
import structlog
from dm_api_account.apis import LoginApi, AccountApi
from helpers.mailhog.mailhog_client import MailHogClient
from dm_api_forum.apis import ForumApi, TopicApi, CommentApi

# from helpers

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False),
    ]
)


@pytest.fixture
def account_api():
    return AccountApi(host='http://localhost:5051')


@pytest.fixture
def login_api():
    return LoginApi(host='http://localhost:5051')


@pytest.fixture
def mailhog():
    return MailHogClient(host='http://localhost:5025')


@pytest.fixture
def forum_api():
    return ForumApi(host='http://localhost:5051')


@pytest.fixture
def topic_api():
    return TopicApi(host='http://localhost:5051')


@pytest.fixture
def comment_api():
    return CommentApi(host='http://localhost:5051')
