def test_put_v1_account_token(dm_api_account, mailhog):
    activation_token = mailhog.get_token_from_last_email()
    response = dm_api_account.account_api.put_v1_account_token(
        token=activation_token
    )
    assert response.status_code == 200
    assert response.json()["resource"]["rating"]["enabled"] is True
