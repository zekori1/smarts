import pprint
import json
import requests

def test_put_v1_account_email():

    headers = {
        'accept': 'text/plain',
        'X-Dm-Auth-Token': 'a63777e4-a7a9-42a5-a46c-a6261a45daae',
        # Already added when you pass json= but not when you pass data=
        # 'Content-Type': 'application/json',
    }

    json_data = {
        'login': 'test_user_1',
        'password': 'test_user_1',
        'email': 'test_user_1@mail.ru',
    }

    response = requests.put('http://localhost:5051/v1/account/email', headers=headers, json=json_data)


def test_delete_v1_account_login():
    headers = {
        'accept': '*/*',
        'X-Dm-Auth-Token': 'IQJh+zgzF5BuAn757nBOvgrFuqIcTY7g35gSlaGbwJsn1xnVTi5xt3xw3C9uGRGo/Mqv8USCAnLoiXihAEwsC1uT8Bt8YzNJcsQ+9rZ0atx3M6UzjnsgWyWQLx889l/bbSvCXkF037o= ',
    }

    response = requests.delete('http://localhost:5051/v1/account/login', headers=headers)

def test_delete_v1_account_login_all():
    headers = {
        'accept': '*/*',
        'X-Dm-Auth-Token': 'IQJh+zgzF5BuAn757nBOvgrFuqIcTY7g35gSlaGbwJsn1xnVTi5xt3xw3C9uGRGo/Mqv8USCAnJFQfktudIgi6WD7hkEI7Ql3rEDrV+zQqbiNO4VcW+Zde8cVlIlQqI5A6/wLA+My0U= ',
    }

    response = requests.delete('http://localhost:5051/v1/account/login/all', headers=headers)
