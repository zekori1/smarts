from jsonmodels.models import Base
from jsonmodels.fields import StringField


class ChangeEmailResponseModel(Base):
    login = StringField()
    password = StringField()
    email = StringField()
