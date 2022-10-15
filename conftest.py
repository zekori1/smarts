import pytest
import structlog

from apis.dm_api_account.models.login.post_v1_account_login_request_model import LoginCredentialsRequestModel
from database.db_3_5 import DmDataBase
from helpers.mailhog.mailhog_client import MailHogClient
from service.dm_api_account import DmApiAccount
from service.dm_api_forum import DmApiForum
from helpers.assertions.assertions import Assertions
from vyper import v
from pathlib import Path

# from helpers


options_list = (
    'service.dm_api_account',
    'service.dm_api_forum',
    'mailhog.host',
)


def set_config(request):
    config = Path(__file__).parent.joinpath('config')
    config_name = request.config.getoption('--env')
    v.set_config_name(config_name)
    v.add_config_path(config)
    v.read_in_config()
    for option in options_list:
        v.set(option, request.config.getoption(f'--{option}'))

    structlog.configure(
        processors=[
            structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False),
        ]
    )


def pytest_addoption(parser):
    parser.addoption('--env', action='store', default='stg')
    for option in options_list:
        parser.addoption(f'--{option}', action='store', default=None)


@pytest.fixture(autouse=True)
def config(request):
    set_config(request)


@pytest.fixture
def mailhog():
    return MailHogClient(host=v.get('mailhog.host'))


@pytest.fixture#(scope='session')
def dm_api_account():
    return DmApiAccount(host=v.get('service.dm_api_account'))


@pytest.fixture#(scope='session')
def dm_api_forum():
    return DmApiForum(host=v.get('service.dm_api_forum'))


db_connection = None


@pytest.fixture
def dm_db():
    global db_connection

    if db_connection is None:
        db_connection = DmDataBase(
            host=v.get('database.postgresql.host'),
            dbname=v.get('database.postgresql.dbname'),
            port=v.get('database.postgresql.port'),
            user=v.get('database.postgresql.user'),
            password=v.get('database.postgresql.password')
        )
    yield db_connection
    # db_connection.close()


@pytest.fixture#(autouse=True)
def token(dm_api_account):
    response = dm_api_account.login_api.post_v1_account_login(
        json_data=LoginCredentialsRequestModel(
            login=v.get('test_user.user_name'),
            password=v.get('test_user.user_password'),

        )
    )
    token = response.headers['X-Dm-Auth-Token']
    dm_api_account.account_api.client.headers = {'X-Dm-Auth-Token':  token}
    return token

@pytest.fixture()
def assertions(dm_db, mailhog):
    return Assertions(db=dm_db, mail_server=mailhog)
