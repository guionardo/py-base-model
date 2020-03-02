from base_model.base_model import BaseModel
from datetime import date, datetime
from uuid import uuid1
from typing import List


class ChildModel(BaseModel):
    """
    id: required
    name: required    
    """
    id: int
    name: str


class ParentModel(BaseModel):
    """
    id: required
    name: required    
    """
    id: int
    name: str
    child: ChildModel
