from dm_api_account.account.account_api import AccountApi
from helpers.mailhog.mailhog_client import MailHogClient


def test_put_v1_account_token():
    account = AccountApi()
    mailhog = MailHogClient()
    activation_token = mailhog.get_token_from_last_email()
    response = account.put_v1_account_token(
        token=activation_token
    )
    assert response.status_code == 200
    assert response.json()["resource"]["rating"]["enabled"] is True
