import uuid
from datetime import datetime
from app.models.__init__ import BaseModel


class User(BaseModel):
    def __init__(self, first_name, last_name: str, email: str, is_admin=False) -> None:
        self.id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
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
        
    def validation(self, first_name, last_name):
        if len(self.first_name) > 50:
            raise ValueError("first_name can't exceed 50 characters")
        elif len(self.last_name) > 50:
            raise ValueError("last_name can't exceed 50 characters")
        elif not isinstance(self.is_admin, bool):
            raise ValueError("You are not admin")
        self.first_name = first_name
        self.last_name - last_name
        self.is_admin = True