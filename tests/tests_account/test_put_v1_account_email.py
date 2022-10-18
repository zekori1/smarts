from vyper import v
from apis.dm_api_account.models.account.put_v1_account_email_request_model import ChangeEmailResponseModel


def test_put_v1_account_email(dm_api_account, dm_db, user_creation, x_dm_auth_token):
    dm_api_account.account_api.put_v1_account_email(
        x_dm_auth_token=x_dm_auth_token,
        json_data=ChangeEmailResponseModel(
            login=v.get('test_user.user_name'),
            password=v.get('test_user.user_password'),
            email=v.get('test_user.user_email')
        )
    )
    rows = dm_db.get_user_by_email(email=v.get('test_user.user_email'))
    assert rows[0]['Email'] == v.get('test_user.user_email')
