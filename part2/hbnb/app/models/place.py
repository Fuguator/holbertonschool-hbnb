import uuid
from datetime import datetime
from app.models.__init__ import BaseModel


class Place(BaseModel):
    def __init__(self, title: str, description: str, price: float, latitude: str, longitude: str, owner) -> None:
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()

    def update(self, data):
        """Update the attributes of the object based on the provided dictionary"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()