from apis.dm_api_account.models.login.post_v1_account_login_request_model import LoginCredentialsRequestModel
from hamcrest import assert_that, has_properties
import pytest

import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False),
    ]
)


# @pytest.mark.parametrize('login, password', [('test_user_10', 'test_user_10')])
def test_post_v1_account_login(dm_api_account, token):
    response = dm_api_account.account_api.get_v1_account()
    assert_that(response.resource, has_properties(
        {
            "login": "test_user_10",
            "roles": [
                "Guest",
                "Player"
            ]
        }
    ))

    # rows = dm_db.get_user_by_login(login=login)
