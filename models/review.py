#!/usr/bin/python3
"""Create user class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Manages user objects"""
    place_id = ""
    user_id = ""
    text = ""
