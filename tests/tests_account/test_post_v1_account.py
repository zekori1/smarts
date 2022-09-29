import pytest

from dm_api_account.models.account.post_v1_account_request_model import RegistrationRequestModel


def test_post_v1_account(dm_api_account, dm_db):
    login = 'test_user_10'
    dm_db.delete_user_by_login(login)
    response = dm_api_account.account_api.post_v1_account(
        json_data=RegistrationRequestModel(
            login='test_user_10',
            email='test_user_10@mail.ru',
            password='test_user_10'
        )
    )
    assert response.status_code == 201


@pytest.mark.parametrize('login, email, password', [('test_user_10', 'test_user_10@mail.ru', 'test_user_10')])
def test_registration_user(login, email, password, dm_api_account, dm_db, mailhog):
    dm_db.delete_user_by_login(login)
    mailhog.delete_all_emails()
    response = dm_api_account.account_api.post_v1_account(
        json_data=RegistrationRequestModel(
            login=login,
            email=email,
            password=password
        )
    )
    token = mailhog.get_token_from_last_email()
    response = dm_api_account.account_api.put_v1_account_token(token=token)
    rows = dm_db.get_user_by_login(login=login)
    for row in rows:
        assert row['Login'] == login, 'User has not registered, he has not in database'
        assert row['Activated'] is True, 'User has not activated'
