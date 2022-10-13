import requests
from restclient.restclient import RestClient
from apis.dm_api_forum.models.topics.post_v1_fora_id_topics import TopicsRequestModel


class ForumApi:
    def __init__(self, host, headers=None):
        self.headers = headers
        self.host = host
        self.client = RestClient(host=self.host)
        if headers:
            self.client.headers = self

    def get_v1_fora(self, x_dm_auth_token):
        headers = {
            'accept': 'text/plain',
            'X-Dm-Auth-Token': x_dm_auth_token,
        }

        response = self.client.get(
            path=f'/v1/fora',
            headers=headers
        )
        return response

    def get_v1_fora_id(self, forum_id):
        headers = {
            'accept': 'text/plain',
        }

        response = self.client.get(
            path=f'/v1/fora/{forum_id}',
            headers=headers
        )
        return response

    def delete_v1_fora_id_comments_unread(self):
        ...

    def get_v1_fora_id_moderators(self):
        headers = {
            'accept': 'text/plain',
        }

        response = self.client.get(
            path=f'/v1/fora/%D0%98%D0%B3%D1%80%D0%BE%D0%B2%D1%8B%D0%B5%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%8B/moderators',
            headers=headers
        )
        return response

    def get_v1_fora_id_topics(self, forum_id):
        headers = {
            'accept': 'text/plain',
        }

        response = self.client.get(
            path=f'/v1/fora/{forum_id}/topics',
            headers=headers
        )
        return response

    def post_v1_fora_id_topics(self, x_dm_auth_token, forum_id, json_data: TopicsRequestModel):
        headers = {
            'accept': 'text/plain',
            'X-Dm-Auth-Token': x_dm_auth_token,
            # Already added when you pass json= but not when you pass data=
            # 'Content-Type': 'application/json',
        }

        # json_data = {
        #     'id': '3fa85f64-5717-4562-b3fc-2c963f66afa6',
        #     'author': {
        #         'login': 'test_user_9',
        #         'roles': [
        #             'Guest',
        #         ],
        #         'mediumPictureUrl': 'string',
        #         'smallPictureUrl': 'string',
        #         'status': 'string',
        #         'rating': {
        #             'enabled': True,
        #             'quality': 0,
        #             'quantity': 0,
        #         },
        #         'online': '2022-09-19T00:55:09.370Z',
        #         'name': 'string',
        #         'location': 'string',
        #         'registration': '2022-09-19T00:55:09.370Z',
        #     },
        #     'created': '2022-09-19T00:55:09.370Z',
        #     'title': 'Я сделал тему с фронта, вернул ее в topic и делаю новую тему через POST',
        #     'description': 'Пробую писать в value, хз че выйдет',
        #     'attached': True,
        #     'closed': True,
        #     'lastComment': {
        #         'created': '2022-09-19T00:55:09.371Z',
        #         'author': {
        #             'login': 'string',
        #             'roles': [
        #                 'Guest',
        #             ],
        #             'mediumPictureUrl': 'string',
        #             'smallPictureUrl': 'string',
        #             'status': 'string',
        #             'rating': {
        #                 'enabled': True,
        #                 'quality': 0,
        #                 'quantity': 0,
        #             },
        #             'online': '2022-09-19T00:55:09.371Z',
        #             'name': 'string',
        #             'location': 'string',
        #             'registration': '2022-09-19T00:55:09.371Z',
        #         },
        #     },
        #     'commentsCount': 0,
        #     'unreadCommentsCount': 0,
        #     'forum': {
        #         'id': 'Общий',
        #         'unreadTopicsCount': 0,
        #     },
        #     'likes': [
        #         {
        #             'login': 'string',
        #             'roles': [
        #                 'Guest',
        #             ],
        #             'mediumPictureUrl': 'string',
        #             'smallPictureUrl': 'string',
        #             'status': 'string',
        #             'rating': {
        #                 'enabled': True,
        #                 'quality': 0,
        #                 'quantity': 0,
        #             },
        #             'online': '2022-09-19T00:55:09.371Z',
        #             'name': 'string',
        #             'location': 'string',
        #             'registration': '2022-09-19T00:55:09.371Z',
        #         },
        #     ],
        # }

        response = self.client.post(
            path=f'/v1/fora/{forum_id}/topics',
            # path=f'/v1/fora/%D0%9E%D0%B1%D1%89%D0%B8%D0%B9/topics',
            headers=headers,
            json=json_data.to_struct()
        )
        return response

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        # data = '{\n  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",\n  "author": {\n    "login": "test_user_9",\n    "roles": [\n      "Guest"\n    ],\n    "mediumPictureUrl": "string",\n    "smallPictureUrl": "string",\n    "status": "string",\n    "rating": {\n      "enabled": true,\n      "quality": 0,\n      "quantity": 0\n    },\n    "online": "2022-09-19T00:55:09.370Z",\n    "name": "string",\n    "location": "string",\n    "registration": "2022-09-19T00:55:09.370Z"\n  },\n  "created": "2022-09-19T00:55:09.370Z",\n  "title": "Я сделал тему с фронта, вернул ее в topic и делаю новую тему через POST",\n  "description": "Пробую писать в value, хз че выйдет",\n  "attached": true,\n  "closed": true,\n  "lastComment": {\n    "created": "2022-09-19T00:55:09.371Z",\n    "author": {\n      "login": "string",\n      "roles": [\n        "Guest"\n      ],\n      "mediumPictureUrl": "string",\n      "smallPictureUrl": "string",\n      "status": "string",\n      "rating": {\n        "enabled": true,\n        "quality": 0,\n        "quantity": 0\n      },\n      "online": "2022-09-19T00:55:09.371Z",\n      "name": "string",\n      "location": "string",\n      "registration": "2022-09-19T00:55:09.371Z"\n    }\n  },\n  "commentsCount": 0,\n  "unreadCommentsCount": 0,\n  "forum": {\n    "id": "Общий",\n    "unreadTopicsCount": 0\n  },\n  "likes": [\n    {\n      "login": "string",\n      "roles": [\n        "Guest"\n      ],\n      "mediumPictureUrl": "string",\n      "smallPictureUrl": "string",\n      "status": "string",\n      "rating": {\n        "enabled": true,\n        "quality": 0,\n        "quantity": 0\n      },\n      "online": "2022-09-19T00:55:09.371Z",\n      "name": "string",\n      "location": "string",\n      "registration": "2022-09-19T00:55:09.371Z"\n    }\n  ]\n}'
        # response = requests.post('http://localhost:5051/v1/fora/%D0%9E%D0%B1%D1%89%D0%B8%D0%B9/topics', headers=headers, data=data)
