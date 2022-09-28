def test_put_v1_account_token(account_api, mailhog):
    activation_token = mailhog.get_token_from_last_email()
    response = account_api.put_v1_account_token(
        token=activation_token
    )
    assert response.status_code == 200
    assert response.json()["resource"]["rating"]["enabled"] is True
