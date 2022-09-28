from dm_api_forum.apis import *


class DmApiForum:

    def __init__(self, host, headers=None):
        self.host = host
        self.headers = headers
        self.forum_api = ForumApi(self.host, self.headers)
        self.comment_api = CommentApi(self.host, self.headers)
        self.topic_api = TopicApi(self.host, self.headers)
