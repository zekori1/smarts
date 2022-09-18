from jsonmodels.models import Base
from jsonmodels.fields import StringField


class RegistrationRequestModel(Base):
    login = StringField()
    email = StringField()
    password = StringField()


m = RegistrationRequestModel(login='123', email='321', password='456')
print(m.to_struct())
