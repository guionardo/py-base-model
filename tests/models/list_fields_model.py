from typing import List

from base_model.base_model import BaseModel
from tests.models.primitive_fields_model import PrimitiveFieldsModel


class ListFieldsModel(BaseModel):
    names: List[str]
    ages: List[int]
    enables: List[bool]


class ListSubModelModel(BaseModel):
    id: int
    submodels: List[PrimitiveFieldsModel]
