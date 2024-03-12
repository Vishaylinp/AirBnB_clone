#!/usr/bin/python3
"""Create user class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Manages City objects"""
    state_id = ""
    name = ""
