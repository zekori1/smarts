import apis.dm_api_forum.apis


class DmApiForum:

    def __init__(self, host, headers=None):
        self.host = host
        self.headers = headers
        self.forum_api = apis.dm_api_forum.apis.ForumApi(self.host, self.headers)
        self.comment_api = apis.dm_api_forum.apis.CommentApi(self.host, self.headers)
        self.topic_api = apis.dm_api_forum.apis.TopicApi(self.host)
