from hamcrest import assert_that, has_properties
from vyper import v
from apis.dm_api_account.models.account.put_v1_account_password_request_model import ChangePasswordResponseModel


def test_put_v1_account_password(dm_api_account, mailhog, dm_db, user_creation, x_dm_auth_token):
    activation_token = mailhog.get_token()
    dm_api_account.account_api.put_v1_account_password(
        x_dm_auth_token=x_dm_auth_token,
        json_data=ChangePasswordResponseModel(
            login=v.get('test_user.user_name'),
            token=activation_token,
            old_password=v.get('test_user.user_password'),
            new_password=v.get('test_user.new_password')
        )
    )
    dm_db.get_user_by_login(login=v.get('test_user.user_name'))
