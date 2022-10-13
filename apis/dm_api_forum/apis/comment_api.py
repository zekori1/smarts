import requests
from restclient.restclient import RestClient


class CommentApi:
    def __init__(self, host='http://localhost:5051', headers=None):
        self.headers = headers
        self.host = host
        self.client = RestClient(host=self.host)
        if headers:
            self.client.headers = self

    def get_v1_forum_comments_id(self):
        headers = {
            'accept': 'text/plain',
        }

        response = requests.get(
            f'{self.host}/v1/forum/comments/14c50c35-0ce3-4925-a2b1-5ad5ea27f8f1',
            headers=headers
        )
        return response

    def post_v1_forum_comments_id_likes(self, x_dm_auth_token):
        headers = {
            'accept': 'text/plain',
            'X-Dm-Auth-Token': x_dm_auth_token,
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        response = requests.post(
            f'{self.host}/v1/forum/comments/14c50c35-0ce3-4925-a2b1-5ad5ea27f8f1/likes',
            headers=headers
        )
        return response

    def patch_v1_forum_comments_id(self, x_dm_auth_token):
        headers = {
            'accept': 'text/plain',
            'X-Dm-Auth-Token': x_dm_auth_token,
            # Already added when you pass json= but not when you pass data=
            # 'Content-Type': 'application/json',
        }

        json_data = {
            'id': '3fa85f64-5717-4562-b3fc-2c963f66afa6',
            'author': {
                'login': 'test_user_7',
                'roles': [
                    'Guest',
                ],
                'mediumPictureUrl': 'string',
                'smallPictureUrl': 'string',
                'status': 'string',
                'rating': {
                    'enabled': True,
                    'quality': 0,
                    'quantity': 0,
                },
                'online': '2022-09-20T21:37:33.115Z',
                'name': 'string',
                'location': 'string',
                'registration': '2022-09-20T21:37:33.115Z',
            },
            'created': '2022-09-20T21:37:33.115Z',
            'updated': '2022-09-20T21:37:33.115Z',
            'text': 'Меняю коммент на вот этот',
            'likes': [
                {
                    'login': 'string',
                    'roles': [
                        'Guest',
                    ],
                    'mediumPictureUrl': 'string',
                    'smallPictureUrl': 'string',
                    'status': 'string',
                    'rating': {
                        'enabled': True,
                        'quality': 0,
                        'quantity': 0,
                    },
                    'online': '2022-09-20T21:37:33.115Z',
                    'name': 'string',
                    'location': 'string',
                    'registration': '2022-09-20T21:37:33.115Z',
                },
            ],
        }

        response = requests.patch(
            f'{self.host}/v1/forum/comments/c3b0db9c-8241-408c-8dfe-9ec0b3c51533',
            headers=headers,
            json=json_data
        )
        return response

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        # data = '{\n  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",\n  "author": {\n    "login": "test_user_7",\n    "roles": [\n      "Guest"\n    ],\n    "mediumPictureUrl": "string",\n    "smallPictureUrl": "string",\n    "status": "string",\n    "rating": {\n      "enabled": true,\n      "quality": 0,\n      "quantity": 0\n    },\n    "online": "2022-09-20T21:37:33.115Z",\n    "name": "string",\n    "location": "string",\n    "registration": "2022-09-20T21:37:33.115Z"\n  },\n  "created": "2022-09-20T21:37:33.115Z",\n  "updated": "2022-09-20T21:37:33.115Z",\n  "text": "Меняю коммент на вот этот",\n  "likes": [\n    {\n      "login": "string",\n      "roles": [\n        "Guest"\n      ],\n      "mediumPictureUrl": "string",\n      "smallPictureUrl": "string",\n      "status": "string",\n      "rating": {\n        "enabled": true,\n        "quality": 0,\n        "quantity": 0\n      },\n      "online": "2022-09-20T21:37:33.115Z",\n      "name": "string",\n      "location": "string",\n      "registration": "2022-09-20T21:37:33.115Z"\n    }\n  ]\n}'
        # response = requests.patch('http://localhost:5051/v1/forum/comments/c3b0db9c-8241-408c-8dfe-9ec0b3c51533', headers=headers, data=data)

    def delete_v1_forum_comments_id_likes(self, x_dm_auth_token):
        headers = {
            'accept': '*/*',
            'X-Dm-Auth-Token': x_dm_auth_token,
        }

        response = requests.delete(
            f'{self.host}/v1/forum/comments/14c50c35-0ce3-4925-a2b1-5ad5ea27f8f1/likes',
            headers=headers
        )
        return response

    def delete_v1_forum_comments_it(self):
        ...
