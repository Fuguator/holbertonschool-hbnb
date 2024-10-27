import uuid
from datetime import datetime
from app.models.__init__ import BaseModel


class Place(BaseModel):
    def __init__(self, title: str, description: str, price: float, latitude: str, longitude: str, owner) -> None:
        super().__init__()
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
    
    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()

    def update(self, data):
        """Update the attributes of the object based on the provided dictionary"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()

    def title_validation(self, text):
        if len(self.title) < 1:
            raise ValueError("title's length is empty")
        elif len(self.title) > 100:
            raise ValueError("title's length is over 100 characters")
        self.title = text

    def price_validation(self, value):
        if self.price < 0:
            raise ValueError("Price can't be negative")
        self.price = value

    def latitude_validation(self, value):
        if len(self.latitude) not in range(-90, 90):
            raise ValueError("latitude must be in range -90 : 90")
        self.latitude = value
        
    def longitude_validation(self, value):
        if len(self.latitude) not in range(-180, 180):
            raise ValueError("longtitude must be in range -180 : 180")
        self.longitude = value
    
    