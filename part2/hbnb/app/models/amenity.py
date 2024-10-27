from typing import Any
import uuid
from datetime import datetime
from app.models.__init__ import BaseModel


class Amenity(BaseModel):
    def __init__(self, name: str) -> None:
        self.id = str(uuid.uuid4())
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
    def name_validation(self, value):
        if len(self.name) not in range(1, 50):
            raise ValueError("invalid name's length")
        self.name = value