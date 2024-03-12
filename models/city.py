#!/usr/bin/python3
"""Create City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """"class that will manage City instances"""

    state_id = ""
    name = ""
