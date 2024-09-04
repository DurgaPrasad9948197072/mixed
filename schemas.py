from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime, date

class RegisterHouseRequest(BaseModel):
    email: EmailStr
    password: str
    username: str

class LoginHouseRequest(BaseModel):
    email: str
    password: str

class UpdateHouseUserRequest(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    status: Optional[int] = None

class HouseOrderRequest(BaseModel):
    id: Optional[int] = None  
    pid: int
    date: Optional[date] = None  
    status: Optional[int] = 0  


class CreatePriceRequest(BaseModel):
    amount: Optional[str] = None
    name: Optional[str] = None
    status: Optional[int] = 0
    description: Optional[str] = None
    key: Optional[str] = None