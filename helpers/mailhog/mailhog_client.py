import json
import requests


class MailHogClient:
    def __init__(self, host='http://localhost:5025'):
        self.host = host

    def get_all_email(self, limit=50):
        params = {
            'limit': str(limit),
        }

        response = requests.get(
            url=f'{self.host}/api/v2/messages',
            params=params,
        )
        return response

    def get_token_from_last_email(self):
        emails = self.get_all_email(limit=1)
        token = json.loads(emails.json()['items'][0]['Content']['Body'])['ConfirmationLinkUrl'].split('/')[-1]
        return token


mailhog = MailHogClient()
# print(mailhog.get_all_email(limit=1).json( ))

# pprint.pprint(mailhog.get_all_email(limit=1).json())


print(mailhog.get_token_from_last_email())
