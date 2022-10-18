from hamcrest import assert_that, has_properties


def test_put_v1_account_token(dm_api_account, user_creation, x_dm_auth_token, mailhog):
    activation_token = mailhog.get_token_from_last_email()
    response = dm_api_account.account_api.put_v1_account_token(
        token=activation_token
    )
    assert_that(response.resource, has_properties(
        {
            "login": "test_user_10"

        }
    ))

