import pprint
import json

import requests


def test_post_v1_account():
    headers = {
        'accept': '*/*',

    }

    json_data = {
        'login': 'test_user_1',
        'email': 'test_user_1@mail.ru',
        'password': 'test_user_1',
    }

    response = requests.post('http://localhost:5051/v1/account', headers=headers, json=json_data)


def test_post_v1_account_user_2():
    headers = {
        'accept': '*/*',

    }

    json_data = {
        'login': 'test_user_2',
        'email': 'test_user_2@mail.ru',
        'password': 'test_user_2',
    }

    response = requests.post('http://localhost:5051/v1/account', headers=headers, json=json_data)


def test_put_v1_account_token():
    headers = {
        'accept': 'text/plain',
    }

    response = requests.put('http://localhost:5051/v1/account/364bddc5-b80d-4283-b179-52e7b602560f', headers=headers)


def test_post_v1_account_login():
    headers = {
        'accept': 'text/plain',
        # Already added when you pass json= but not when you pass data=
        # 'Content-Type': 'application/json',
    }

    json_data = {
        'login': 'test_user_1',
        'password': 'test_user_1',
        'rememberMe': True,
    }

    response = requests.post('http://localhost:5051/v1/account/login', headers=headers, json=json_data)


def test_get_v1_account():
    headers = {
        'accept': 'text/plain',
        'X-Dm-Auth-Token': 'IQJh+zgzF5Dyc40I/E9cQ/yXxbYHhOjtxXvECp5cuKqKRfH3p9aGZ9qpuBQLeImhImw8igaYPFZfdQ7x8aDHtnPeXaxRvQ/+ffJHsWxGUKyRCNFjXcGOC6LTstkLuxnI5khOnwdTFiA=',
    }

    response = requests.get('http://localhost:5051/v1/account', headers=headers)
    print()
    # pprint.pprint(response.text)
    # print(response.headers )
    # print(response.status_code)
    pprint.pprint(response.json())
    print(response.url)
    print(response.content)


def test_get_all_email():
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
    print()
    pprint.pprint(token)
    return token
