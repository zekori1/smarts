from jsonmodels.models import Base
from jsonmodels.fields import StringField


class ResetPasswordResponseModel(Base):
    login = StringField()
    email = StringField()
