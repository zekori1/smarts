import requests


class TopicApi:
    def __init__(self, host='http://localhost:5051'):
        self.host = host

    def get_v1_topics_id(self, x_dm_auth_token):
        headers = {
            'accept': 'text/plain',
            'X-Dm-Auth-Token': x_dm_auth_token,
        }

        response = requests.get(
            f'{self.host}/v1/topics/ebfef5f8-7f7d-42df-ab1a-081bf8da8ad7',
            headers=headers
        )
        return response

    def patch_v1_topics_id(self, x_dm_auth_token):
        headers = {
            'accept': 'text/plain',
            'X-Dm-Auth-Token': x_dm_auth_token,
            # Already added when you pass json= but not when you pass data=
            # 'Content-Type': 'application/json',
        }

        json_data = {
            'id': '3fa85f64-5717-4562-b3fc-2c963f66afa6',
            'author': {
                'login': 'test_user_9',
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
                'online': '2022-09-19T18:02:00.668Z',
                'name': 'string',
                'location': 'string',
                'registration': '2022-09-19T18:02:00.668Z',
            },
            'created': '2022-09-19T18:02:00.668Z',
            'title': 'Я сделал тему с фронта, вернул ее в topic и делаю новую тему через POST и сейчас меняю',
            'description': 'Пробую писать в value, хз че выйдет. Меняю тему',
            'attached': True,
            'closed': True,
            'lastComment': {
                'created': '2022-09-19T18:02:00.668Z',
                'author': {
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
                    'online': '2022-09-19T18:02:00.668Z',
                    'name': 'string',
                    'location': 'string',
                    'registration': '2022-09-19T18:02:00.668Z',
                },
            },
            'commentsCount': 0,
            'unreadCommentsCount': 0,
            'forum': {
                'id': 'Общий',
                'unreadTopicsCount': 0,
            },
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
                    'online': '2022-09-19T18:02:00.668Z',
                    'name': 'string',
                    'location': 'string',
                    'registration': '2022-09-19T18:02:00.668Z',
                },
            ],
        }

        response = requests.patch(
            f'{self.host}/v1/topics/88e95695-8f9c-4477-9bcc-703cf7a55b0b',
            headers=headers,
            json=json_data
        )
        return response

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        # data = '{\n  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",\n  "author": {\n    "login": "test_user_9",\n    "roles": [\n      "Guest"\n    ],\n    "mediumPictureUrl": "string",\n    "smallPictureUrl": "string",\n    "status": "string",\n    "rating": {\n      "enabled": true,\n      "quality": 0,\n      "quantity": 0\n    },\n    "online": "2022-09-19T18:02:00.668Z",\n    "name": "string",\n    "location": "string",\n    "registration": "2022-09-19T18:02:00.668Z"\n  },\n  "created": "2022-09-19T18:02:00.668Z",\n  "title": "Я сделал тему с фронта, вернул ее в topic и делаю новую тему через POST и сейчас меняю",\n  "description": "Пробую писать в value, хз че выйдет. Меняю тему",\n  "attached": true,\n  "closed": true,\n  "lastComment": {\n    "created": "2022-09-19T18:02:00.668Z",\n    "author": {\n      "login": "string",\n      "roles": [\n        "Guest"\n      ],\n      "mediumPictureUrl": "string",\n      "smallPictureUrl": "string",\n      "status": "string",\n      "rating": {\n        "enabled": true,\n        "quality": 0,\n        "quantity": 0\n      },\n      "online": "2022-09-19T18:02:00.668Z",\n      "name": "string",\n      "location": "string",\n      "registration": "2022-09-19T18:02:00.668Z"\n    }\n  },\n  "commentsCount": 0,\n  "unreadCommentsCount": 0,\n  "forum": {\n    "id": "Общий",\n    "unreadTopicsCount": 0\n  },\n  "likes": [\n    {\n      "login": "string",\n      "roles": [\n        "Guest"\n      ],\n      "mediumPictureUrl": "string",\n      "smallPictureUrl": "string",\n      "status": "string",\n      "rating": {\n        "enabled": true,\n        "quality": 0,\n        "quantity": 0\n      },\n      "online": "2022-09-19T18:02:00.668Z",\n      "name": "string",\n      "location": "string",\n      "registration": "2022-09-19T18:02:00.668Z"\n    }\n  ]\n}'
        # response = requests.patch('http://localhost:5051/v1/topics/88e95695-8f9c-4477-9bcc-703cf7a55b0b', headers=headers, data=data)

    def delete_v1_topics_id(self):
        ...

    def post_v1_topics_id_likes(self, x_dm_auth_token):
        headers = {
            'accept': 'text/plain',
            'X-Dm-Auth-Token': x_dm_auth_token,
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        response = requests.post(
            f'{self.host}/v1/topics/88e95695-8f9c-4477-9bcc-703cf7a55b0b/likes',
            headers=headers
        )
        return response

    def delete_v1_topics_id_likes(self, x_dm_auth_token):
        headers = {
            'accept': '*/*',
            'X-Dm-Auth-Token': x_dm_auth_token,
        }

        response = requests.delete(
            f'{self.host}/v1/topics/88e95695-8f9c-4477-9bcc-703cf7a55b0b/likes',
            headers=headers
        )
        return response

    def post_v1_topics_id_comments(self, x_dm_auth_token):
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
                'online': '2022-09-19T21:53:33.890Z',
                'name': 'string',
                'location': 'string',
                'registration': '2022-09-19T21:53:33.890Z',
            },
            'created': '2022-09-19T21:53:33.890Z',
            'updated': '2022-09-19T21:53:33.890Z',
            'text': 'Хуй знает, выйдет или нет, делаю первый коммент',
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
                    'online': '2022-09-19T21:53:33.890Z',
                    'name': 'string',
                    'location': 'string',
                    'registration': '2022-09-19T21:53:33.890Z',
                },
            ],
        }

        response = requests.post(
            f'{self.host}/v1/topics/88e95695-8f9c-4477-9bcc-703cf7a55b0b/comments',
            headers=headers,
            json=json_data
        )
        return response

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        # data = '{\n  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",\n  "author": {\n    "login": "test_user_7",\n    "roles": [\n      "Guest"\n    ],\n    "mediumPictureUrl": "string",\n    "smallPictureUrl": "string",\n    "status": "string",\n    "rating": {\n      "enabled": true,\n      "quality": 0,\n      "quantity": 0\n    },\n    "online": "2022-09-19T21:53:33.890Z",\n    "name": "string",\n    "location": "string",\n    "registration": "2022-09-19T21:53:33.890Z"\n  },\n  "created": "2022-09-19T21:53:33.890Z",\n  "updated": "2022-09-19T21:53:33.890Z",\n  "text": "Хуй знает, выйдет или нет, делаю первый коммент",\n  "likes": [\n    {\n      "login": "string",\n      "roles": [\n        "Guest"\n      ],\n      "mediumPictureUrl": "string",\n      "smallPictureUrl": "string",\n      "status": "string",\n      "rating": {\n        "enabled": true,\n        "quality": 0,\n        "quantity": 0\n      },\n      "online": "2022-09-19T21:53:33.890Z",\n      "name": "string",\n      "location": "string",\n      "registration": "2022-09-19T21:53:33.890Z"\n    }\n  ]\n}'
        # response = requests.post('http://localhost:5051/v1/topics/88e95695-8f9c-4477-9bcc-703cf7a55b0b/comments', headers=headers, data=data)

    def get_v1_topics_id_comments(self, x_dm_auth_token):
        headers = {
            'accept': 'text/plain',
            'X-Dm-Auth-Token': x_dm_auth_token,
        }

        response = requests.get(
            f'{self.host}/v1/topics/88e95695-8f9c-4477-9bcc-703cf7a55b0b/comments',
            headers=headers
        )
        return response

    def delete_v1_topics_id_comments_unread(self, x_dm_auth_token):
        headers = {
            'accept': '*/*',
            'X-Dm-Auth-Token': x_dm_auth_token,
        }

        response = requests.delete(
            f'{self.host}/v1/topics/88e95695-8f9c-4477-9bcc-703cf7a55b0b/comments/unread',
            headers=headers
        )
        return response
