from base_model.base_model import BaseModel
from datetime import date, datetime
from uuid import uuid1
from typing import List


class TestModel(BaseModel):
    """
    id: required default=0
    name: default="empty name"
    date: default=MIN_TIMESTAMP
    date_time: default=MIN_TIMESTAMP
    guid: default=self.uuid1()
    """

    id: int
    name: str
    date: date
    date_time: datetime
    guid: str
    names: List[str]

    def uuid1(self):
        return str(uuid1())
