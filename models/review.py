#!/usr/bin/python3
"""Create user class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """"class that will manage Review instances"""
    place_id = ""
    user_id = ""
    text = ""
