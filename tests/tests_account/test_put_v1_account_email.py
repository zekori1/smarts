from apis.dm_api_account import LoginCredentialsRequestModel
from apis.dm_api_account.models.account.put_v1_account_email_request_model import ChangeEmailResponseModel
import pytest

import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False),
    ]
)


@pytest.mark.parametrize('login, password, email, remember_me',
                         [('test_user_10', 'test_user_10', 'test_user_xui@mail.ru', True)])
def test_post_v1_account_login(dm_api_account, dm_db, login, password, email, remember_me):
    response = dm_api_account.login_api.post_v1_account_login(
        json_data=LoginCredentialsRequestModel(
            login=login,
            password=password,
            remember_me=remember_me
        )
    )
    x_dm = response.headers.get('X-Dm-Auth-Token')
    print(x_dm)

    response = dm_api_account.account_api.put_v1_account_email(
        x_dm_auth_token=x_dm,
        json_data=ChangeEmailResponseModel(
            login=login,
            password=password,
            email=email
        )
    )
    assert response.status_code == 200
    rows = dm_db.get_user_by_email(email=email)
    assert rows[0]['Email'] == email
