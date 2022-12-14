from hamcrest import assert_that, has_properties


def test_get_v1_account(dm_api_account, user_creation, x_dm_auth_token):
    response = dm_api_account.account_api.get_v1_account(x_dm_auth_token=x_dm_auth_token)
    assert_that(response.resource, has_properties(
        {
            "login": "test_user_10",
            "roles": [
                "Guest",
                "Player"
            ]
        }
    ))
