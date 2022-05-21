#!/usr/bin/env python3
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    first_name: str
    last_name: str
    email: str
    street: str
    phone: str

class UpdateUser(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    street: Optional[str] = None
    phone: Optional[str] = None
