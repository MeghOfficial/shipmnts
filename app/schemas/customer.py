from pydantic import BaseModel, ConfigDict

class CustomerCreate(BaseModel):
    name: str
    category: str
    address: str
    opening_balance : float


class CustomerResponse(BaseModel):
    id: int
    name: str
    category: str
    address: str
    opening_balance : float

    model_config = ConfigDict(from_attributes=True)

