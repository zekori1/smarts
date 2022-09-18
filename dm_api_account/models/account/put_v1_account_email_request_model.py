from jsonmodels.models import Base
from jsonmodels.fields import StringField, IntField, FloatField, EmbeddedField, ListField, BoolField, DateField


class Rating(Base):
    enabled = BoolField()
    quality = IntField()
    quantity = IntField()


def roles_put_account_email_validator(value):
    some = ['Guest', 'Player', 'Administrator', 'NannyModerator', 'RegularModerator', 'SeniorModerator']
    for item in value:
        if item not in some:
            raise ValueError(f'Значение {item} не в списке допустимых значений some')


class User(Base):
    login = StringField()
    roles = ListField(str, validators=[roles_put_account_email_validator])
    medium_picture_url = StringField(name='mediumPictureUrl')
    small_picture_url = StringField(name='smallPictureUrl')
    status = StringField()
    rating = EmbeddedField(Rating)
    online = DateField()
    name = StringField()
    location = StringField()
    registration = DateField()


class UserEnvelopeResponseModel(Base):
    resource = EmbeddedField(User)
    metadata = StringField()
