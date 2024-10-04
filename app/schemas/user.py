from pydantic import BaseModel, EmailStr
from typing import List,Optional
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

class FeatureRequest(BaseModel):
    name: str
    status: Optional[int] = 0

class TechnicalRequest(BaseModel):
    name: str
    status: Optional[int] = 0

class CompatibilityRequest(BaseModel):
    name: str
    status: Optional[int] = 0

class ProductHouseRequest(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None
    price: Optional[CreatePriceRequest] = None
    features: Optional[List[FeatureRequest]] = []
    technical: Optional[List[TechnicalRequest]] = []
    compatibility: Optional[List[CompatibilityRequest]] = []