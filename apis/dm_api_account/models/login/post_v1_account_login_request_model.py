from jsonmodels.models import Base
from jsonmodels.fields import StringField, BoolField


class LoginCredentialsRequestModel(Base):
    login = StringField()
    password = StringField()
    remember_me = BoolField(name='rememberMe', default=True)
