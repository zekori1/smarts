from datetime import datetime

from jsonmodels.models import Base
from jsonmodels.fields import StringField, IntField, FloatField, EmbeddedField, ListField, BoolField, DateField


def info_db_text_validator(value):
    info_bb_text = ['Common', 'Info', 'Post', 'Chat', '']
    if value not in info_bb_text:
        raise ValueError


def roles_validator(value):
    some = ['Guest', 'Player', 'Administrator', 'NannyModerator', 'RegularModerator', 'SeniorModerator']
    for item in value:
        if item not in some:
            raise ValueError(f'Значение {item} не в списке допустимых значений some')


class Forum(Base):
    id = StringField()
    unread_topics_count = IntField(name='unreadTopicsCount', default=0)


class CommonBbText(Base):
    value = StringField()
    parse_mode = StringField(name='parseMode', validators=[info_db_text_validator])


class Rating(Base):
    enabled = BoolField(default=True)
    quality = IntField(default=0)
    quantity = IntField(default=0)


class User(Base):
    login = StringField()
    roles = ListField(str, validators=[roles_validator])
    medium_picture_url = StringField(name='mediumPictureUrl', default='')
    small_picture_url = StringField(name='smallPictureUrl', default='')
    status = StringField(default='')
    rating = EmbeddedField(Rating, default=Rating())
    online = DateField(default=datetime.now())
    name = StringField(default='')
    location = StringField(default='')
    registration = DateField(default=datetime.now())


class LastTopicComment(Base):
    created = DateField(default=datetime.now())
    author = EmbeddedField(User, default=User())


class TopicsRequestModel(Base):
    id = StringField()
    author = EmbeddedField(User, default=User())
    created = DateField(default=datetime.now())
    title = StringField()
    description = StringField(str, default='')
    attached = BoolField(default=True)
    closed = BoolField(default=True)
    lastComment = EmbeddedField(LastTopicComment, default=LastTopicComment())
    comments_count = IntField(name='commentsCount')
    unread_comments_count = IntField(name='unreadCommentsCount')
    forum = EmbeddedField(Forum, default=Forum())
    likes = ListField(EmbeddedField(User, str, default=User()))
