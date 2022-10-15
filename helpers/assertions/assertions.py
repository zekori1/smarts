from hamcrest import has_entries, assert_that


class Assertions:
    def __init__(self, db, mail_server):
        self.db = db
        self.mail_server = mail_server

    def assert_db_state(self, email, login):
        rows = self.db.get_user_by_login(login=login)
        for row in rows:
            assert_that(row, has_entries(
                {
                    'Login': login,
                    'Activated': True,
                    'Email': email
                }

            ))

    def assert_all(self, email, login):
        user_email = self.mail_server.get_email_by_user_name(user_name=login)
        assert user_email
        rows = self.db.get_user_by_login(login=login)
        for row in rows:
            assert_that(row, has_entries(
                {
                    'Login': login,
                    'Activated': True,
                    'Email': email
                }

            ))
