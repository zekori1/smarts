import inspect
import uuid
import records
import structlog
from typing import List, Dict


class DmDataBase:
    def __init__(self, host, dbname, user, password, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.db = records.Database(f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}")
        self.log = structlog.get_logger(self.__class__.__name__).bind(service='db')

    def close(self):
        self.db.close()

    def _send_query(self, query):
        log = self.log.bind(request_id=str(uuid.uuid4()))
        log.msg(
            'request',
            caller=inspect.stack()[2][3],
        )
        print(query)
        result = self.db.query(query)
        if result is not None:
            print(result.dataset)
        return result

    def _send_bulk_query(self, query):
        log = self.log.bind(request_id=str(uuid.uuid4()))
        log.msg(
            'request',
            caller=inspect.stack()[2][3],
        )
        print(query)
        self.db.bulk_query(query)

    def get_all_users(self):
        query = '''
        SELECT * 
        FROM "public"."Users"
        '''
        rows = self._send_query(query).as_dict()
        return rows

    def delete_user_by_login(self, login):
        query = f'''
        DELETE
        FROM "public"."Users"
        WHERE "Login" = '{login}'
        '''
        self._send_bulk_query(query)

    def get_user_by_login(self, login: str) -> List[Dict]:
        query = f'''
              SELECT * 
              FROM "public"."Users"
              WHERE "Login" = '{login}'
              '''
        rows = self._send_query(query).as_dict()
        return rows

    def get_user_by_email(self, email: str) -> List[Dict]:
        query = f'''
              SELECT * 
              FROM "public"."Users"
              WHERE "Email" = '{email}'
              '''
        rows = self._send_query(query).as_dict()
        return rows
