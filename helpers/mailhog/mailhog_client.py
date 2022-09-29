import json
import re
import requests
from restclient.restclient import RestClient


class MailHogClient:
    def __init__(self, host, headers=None):
        self.headers = headers
        self.host = host
        self.client = RestClient(host=self.host)
        if headers:
            self.client.headers = self

    def get_all_email(self, limit=50):
        params = {
            'limit': str(limit),
        }

        response = self.client.get(
            path=f'/api/v2/messages',
            params=params,
        )
        return response

    def get_token_from_last_email(self):
        emails = self.get_all_email(limit=1)
        token = json.loads(emails.json()['items'][0]['Content']['Body'])['ConfirmationLinkUrl'].split('/')[-1]
        return token

    def get_token(self, user='test_user_8', token_type='password'):

        response = self.get_all_email()
        token = None

        for email in response.json()['items']:
            content = json.loads(email['Content']['Body'])
            if re.findall(f'ConfirmationLinkUri.*{token_type}', str(content)):
                if content['Login'] == user:
                    token = content['ConfirmationLinkUri'].split('/')[-1]
        return token

    def delete_email_by_id(self, email_id):

        response = self.client.delete(
            path=f'/api/v1/messages/{email_id}',
        )
        return response

    def delete_all_emails(self):
        emails_ids = [_['ID'] for _ in self.get_all_email().json()['items']]
        for email_id in emails_ids:
            self.delete_email_by_id(email_id=email_id)
