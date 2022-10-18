import pytest
from apis.dm_api_account.models.account.post_v1_account_request_model import RegistrationRequestModel
from hamcrest import assert_that, has_entries


def test_post_v1_account(dm_api_account, dm_db):
    login = 'test_user_10'
    dm_db.delete_user_by_login(login)
    dm_api_account.account_api.post_v1_account(
        json_data=RegistrationRequestModel(
            login='test_user_10',
            email='test_user_10@mail.ru',
            password='test_user_10'
        )
    )


@pytest.mark.parametrize('login, email, password', [('test_user_10', 'test_user_10@mail.ru', 'test_user_10')])
def test_registration_user_check_all(login, email, password, dm_api_account, dm_db, mailhog, assertions):
    dm_db.delete_user_by_login(login)
    mailhog.delete_all_emails()
    dm_api_account.account_api.post_v1_account(
        json_data=RegistrationRequestModel(
            login=login,
            email=email,
            password=password
        )
    )
    user_email = mailhog.get_email_by_user_name(user_name=login)
    assert user_email
    token = mailhog.get_token_from_email(user_email[0])
    dm_api_account.account_api.put_v1_account_token(token=token)
    assertions.assert_all(email, login)


@pytest.mark.parametrize('login, email, password', [('test_user_10', 'test_user_10@mail.ru', 'test_user_10')])
def test_registration_user_check_db_state(login, email, password, dm_api_account, dm_db, mailhog, assertions):
    dm_db.delete_user_by_login(login)
    mailhog.delete_all_emails()
    dm_api_account.account_api.post_v1_account(
        json_data=RegistrationRequestModel(
            login=login,
            email=email,
            password=password
        )
    )
    user_email = mailhog.get_email_by_user_name(user_name=login)
    assert user_email
    token = mailhog.get_token_from_email(user_email[0])
    dm_api_account.account_api.put_v1_account_token(token=token)
    assertions.assert_db_state(email, login)
