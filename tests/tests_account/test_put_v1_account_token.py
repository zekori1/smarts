from dm_api_account.apis.account.account_api import AccountApi
from helpers.mailhog.mailhog_client import MailHogClient
from dm_api_account.models.account.put_v1_account_token_request_model import UserEnvelopeResponseModel


def test_put_v1_account_token():
    account = AccountApi()
    mailhog = MailHogClient()
    activation_token = mailhog.get_token_from_last_email()
    response = account.put_v1_account_token(
        token=activation_token
    )
    assert response.status_code == 200
    assert response.json()["resource"]["rating"]["enabled"] is True
