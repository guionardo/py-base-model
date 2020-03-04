from typing import Dict

from base_model.base_model import BaseModel


class DictFieldsModel(BaseModel):
    names: Dict[str, str]
    ages: Dict[str, int]
    enables: Dict[str, bool]
