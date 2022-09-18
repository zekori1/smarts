import json
import pprint

import requests


def test_get_all_email(limit=50):
    params = {
        'limit': str(limit),
    }

    response = requests.get(
        url='http://localhost:5025/api/v2/messages',
        params=params,
    )
    return response


def test_get_token_from_last_email():
    emails = test_get_all_email(limit=1)
    token = json.loads(emails.json()['items'][0]['Content']['Body'])['ConfirmationLinkUrl'].split('/')[-1]
    return token


# mailhog = MailHogClient()
# print(mailhog.get_token_from_last_email())

# print(mailhog.get_all_email(limit=1).json( ))
# pprint.pprint(mailhog.get_all_email(limit=1).json())

