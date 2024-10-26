import uuid
from datetime import datetime
from app.models.__init__ import BaseModel


class Reviev(BaseModel):
    def __init__(self, text: str, rating: int, place, user) -> None:
        self.id = str(uuid.uuid4())
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user
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