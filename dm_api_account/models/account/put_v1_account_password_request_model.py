from jsonmodels.models import Base
from jsonmodels.fields import StringField


class ChangePasswordResponseModel(Base):
    login = StringField()
    token = StringField()
    old_password = StringField(name='oldPassword')
    new_password = StringField(name='newPassword')
