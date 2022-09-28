import json
import re
import requests


class MailHogClient:
    def __init__(self, host):
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

    def get_token(self, user='test_user_8', token_type='password'):

        response = self.get_all_email()
        token = None

        for email in response.json()['items']:
            content = json.loads(email['Content']['Body'])
            if re.findall(f'ConfirmationLinkUri.*{token_type}', str(content)):
                if content['Login'] == user:
                    token = content['ConfirmationLinkUri'].split('/')[-1]
        return token

# mailhog = MailHogClient()
# # # # print(mailhog.get_token_from_last_email())
# client = MailHogClient()
# response = client.get_all_email()
# #
# user = input('Введи имя пользователя:')
#
#
# def get_token(user, token_type):
#     response = client.get_all_email()
#     token = None
#
#     for email in response.json()['items']:
#         content = json.loads(email['Content']['Body'])
#         if re.findall(f'ConfirmationLinkUri.*{token_type}', str(content)):
#             if content['Login'] == user:
#                 token = content['ConfirmationLinkUri'].split('/')[-1]
#     return token
#
#
# print(get_token(user, 'password'))


# print(mailhog.get_all_email(limit=1).json( ))
# pprint.pprint(mailhog.get_all_email(limit=1).json())

# def get_token_from_email_password(self):
#     emails = self.get_all_email(limit=5)
#     for email in response.json['items']:
# token = json.loads(emails.json()['items'][0]['Content']['Body'])['ConfirmationLinkUrl'].split('/')[-1]
# pprint.pprint(emails.json()['items'])
# i = emails.json()['items']
# pprint.pprint(emails.content)
# token_every = json.loads(emails.json()['items'][0]['Content']['Body'])['Login']
# emails_slov  = emails
# print(emails_slov)
# for item in i:
#     print(item, '->', i.values())
# for kluch, letter in emails_slov.items():
#     if kluch == '_content':
#         print(letter)
#         # for kluchh, znachenie in letter.items():
#         #     if kluchh == 'items':
#         #         print(znachenie)

#     print(item)
# pprint.pprint(emails_slov)

# while token_every == 'test_uses_6':
#     print(token_every)

# print(i)
# token_every = json.loads(emails.json()['items'][0]['Content']['Body'])['Login']
# for item in
# print(token_every)
# pprint.pprint(emails.json())
# return json.load()
# token = json.loads(emails.json()['items'][0])
# return json
# print(emails.json()['items'])
# print(emails.raw)

# print(emails.request())

# mailhog = MailHogClient()
# print(mailhog.get_token_from_email_password())
