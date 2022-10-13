from jsonmodels.models import Base
from jsonmodels.fields import StringField, IntField, FloatField, EmbeddedField, ListField, BoolField, DateField


class PagingSettings(Base):
    posts_per_page = IntField(name='postsPerPage')
    comments_per_page = IntField(name='commentsPerPage')
    topics_per_page = IntField(name='topicsPerPage')
    messages_per_page = IntField(name='messagesPerPage')
    entities_per_page = IntField(name='entitiesPerPage')


def user_settings_validator(value):
    color_schema = ['Modern', 'Pale', 'Classic', 'ClassicPale', 'Night']
    if value not in color_schema:
        raise KeyError


class UserSettings(Base):
    color_schema = StringField(name='colorSchema', validators=[user_settings_validator])  # add
    nanny_greetings_message = StringField(name='nannyGreetingsMessage')
    paging = EmbeddedField(PagingSettings)


def info_db_text_validator(value):
    info_bb_text = ['Common', 'Info', 'Post', 'Chat', '']
    if value not in info_bb_text:
        raise ValueError


class InfoDbText(Base):
    value = StringField()
    parse_mode = StringField(name='parseMode', validators=[info_db_text_validator])  # adv


class Rating(Base):
    enabled = BoolField()
    quality = IntField()
    quantity = IntField()


def roles_validator(value):
    some = ['Guest', 'Player', 'Administrator', 'NannyModerator', 'RegularModerator', 'SeniorModerator']
    for item in value:
        if item not in some:
            raise ValueError(f'Значение {item} не в списке допустимых значений some')


class UserDetails(Base):
    login = StringField()
    roles = ListField(str, validators=[roles_validator])
    medium_picture_url = StringField(name='mediumPictureUrl')
    small_picture_url = StringField(name='smallPictureUrl')
    status = StringField()
    rating = EmbeddedField(Rating)
    online = DateField()
    name = StringField()
    location = StringField()
    registration = DateField()
    icq = StringField()
    skype = StringField()
    original_picture_url = StringField(name='originalPictureUrl')
    info = EmbeddedField([InfoDbText, str])
    settings = EmbeddedField(UserSettings)


class UserDetailsEnvelopeResponseModel(Base):
    resource = EmbeddedField(UserDetails)
    metadata = StringField()
