from datetime import datetime, date, time

from base_model.base_model import BaseModel


class TimeFieldsModel(BaseModel):
    birthday: date
    register: datetime
    alarm: time
