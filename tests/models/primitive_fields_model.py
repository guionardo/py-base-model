from base_model.base_model import BaseModel


class PrimitiveFieldsModel(BaseModel):
    id: int
    name: str
    active: bool
    size: float
