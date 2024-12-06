from pydantic import BaseModel, EmailStr
from typing import List,Optional,Union,Dict
from datetime import datetime, date

class RegisterHouseRequest(BaseModel):
    email: EmailStr
    password: str
    username: str

class LoginHouseRequest(BaseModel):
    email: str
    password: str

class UpdateHouseUserRequest(BaseModel):
    username: Optional[str] = None
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

class UpdateProductHouseRequest(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None
    price: Optional[str] = None
    features: Optional[List[FeatureRequest]] = []
    technical: Optional[List[TechnicalRequest]] = []
    compatibility: Optional[List[CompatibilityRequest]] = []

class UpdateHouseSettingsRequest(BaseModel):
    field: str
    value: str
    uid: int

class OTPRequest(BaseModel):
    email: EmailStr
    id: int

class OTPVerify(BaseModel):
    id: int
    otp: str

class SearchQuery(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    min_price: Optional[float] = None
    max_price: Optional[float] = None


class CreateSubscriptionRequest(BaseModel):
    user_id: int
    product_id: int
    plan_name: str
    amount: float
    payment_method: str
    type_payment: Optional[str]=None
    status: str
    billing_cycle: str  # monthly, quarterly, annually
    billing_date: datetime
    expiration_date: datetime
    current_price: float
    selected_features: Optional[List[int]] = None


class ImageDeletionResponse(BaseModel):
    result: str


class OfferCreate(BaseModel):
    discountPercentage: int
    startDate: str
    endDate: str
    id: int

class OfferUpdate(BaseModel):
    discountPercentage: int
    startDate: str
    endDate: str
    id:int

class OfferResponse(BaseModel):
    id: int
    poid: int
    discountPercentage: str
    startDate: str
    endDate: str


class ReviewRequest(BaseModel):
    status: int
    notes: Optional[str] = None


class EmailRequest(BaseModel):
    from_email: str
    to_email: str
    subject: str
    body: str

class Feature(BaseModel):
    feid: Optional[int] = None
    name: str
    price: float
    plan_id: Optional[int] = None

class FeaturesRequest(BaseModel):
    features: list[Feature]

class Plan(BaseModel):
    pid: Optional[int] = None
    name: str
    base_price: float
    description: Optional[str] = None
    planscheme_id: int
    includedFeatures: Optional[List[int]] = None


class CustomizationRequestPayload(BaseModel):
    poid: int  # Template ID
    id: int  # Customization ID
    customizationRequests: Dict[str, List[str]]  # Customization groups with descriptions


# Define CustomizationDetail with fields for customization and status
class CustomizationDetail(BaseModel):
    customization: str  # The customization string
    status: Dict[str, Union[int, int]]  # Status includes both value and rid (Request ID)

# CustomizationGroup should align with the updated CustomizationDetail structure
class CustomizationGroup(BaseModel):
    name: str  # Group name
    customizations: List[CustomizationDetail]  # List of CustomizationDetail objects


class ProductDetails(BaseModel):
    poid: int
    name: str
    description: str
    category: str
    image: str

class UserDetails(BaseModel):
    user_id: int
    username: str
    email: str

class CustomizationRequestResponse(BaseModel):
    user_details: UserDetails
    product_details: ProductDetails
    customization_requests: List[CustomizationGroup]


# Define the Pydantic model for the request body
class UpdateCustomizationStatusRequest(BaseModel):
    rid: int
    new_status: int


# Request model
class PasswordResetRequest(BaseModel):
    email: EmailStr

# Reset password form model
class PasswordResetForm(BaseModel):
    token: str
    new_password: str