import pytest
import structlog
from helpers.mailhog.mailhog_client import MailHogClient
from service.dm_api_account import DmApiAccount
from service.dm_api_forum import DmApiForum
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


@pytest.fixture
def dm_api_account():
    return DmApiAccount(host=v.get('service.dm_api_account'))


@pytest.fixture
def dm_api_forum():
    return DmApiForum(host=v.get('service.dm_api_forum'))
