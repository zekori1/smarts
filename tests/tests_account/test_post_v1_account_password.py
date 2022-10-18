from vyper import v
from apis.dm_api_account.models.account.post_v1_account_password_request_model import ResetPasswordResponseModel


def test_post_v1_account_password(dm_api_account, dm_db, user_creation, x_dm_auth_token):
    dm_api_account.account_api.post_v1_account_password(
        x_dm_auth_token=x_dm_auth_token,
        json_data=ResetPasswordResponseModel(
            login=v.get('test_user.user_name'),
            email=v.get('test_user.user_email')
        )

    )
    dm_db.get_user_by_login(login=v.get('test_user.user_name'))
    dm_db.get_user_by_email(email=v.get('test_user.user_email'))
