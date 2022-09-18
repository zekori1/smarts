from jsonmodels.models import Base
from jsonmodels.fields import StringField, BoolField


class GeneralErrorRequestModel(Base):
    message = StringField()
