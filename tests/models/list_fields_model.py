from typing import List

from base_model.base_model import BaseModel


class ListFieldsModel(BaseModel):
    names: List[str]
    ages: List[int]
    enables: List[bool]
