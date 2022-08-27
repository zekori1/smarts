import requests
import json
import pprint


def get_all_email():
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    params = {
        'limit': '50',
    }

    response = requests.get('http://localhost:5025/api/v2/messages', params=params, headers=headers)
    # pprint.pprint(response.json())
    emails = response.json()
    items = emails['items']
    content_user = items[0]
    content = content_user['Content']
    body = content['Body']
    qson = json.loads(body)
    confirmation_link_url = qson['ConfirmationLinkUrl']
    token = confirmation_link_url.split('/')[-1]
    return token

print(get_all_email())