from typing import Optional
from pydantic import BaseModel

class TraineeModel(BaseModel):
    type_document: str
    document: str
    name: str
    lastname: str
    program: str
    record_number: int
    
class TraineeUpdateModel(BaseModel):
    type_document: Optional[str] = None
    name: Optional[str] = None
    lastname: Optional[str] = None
    program: Optional[str] = None
    record_number: Optional[int] = None
    

    