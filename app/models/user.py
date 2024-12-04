from sqlalchemy import Column, Integer, String, TIMESTAMP, Date, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base
from datetime import datetime

class Houseuser(Base):
    __tablename__ = "houseuser"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(225), nullable=True)
    email = Column(String(225), nullable=True)
    password = Column(String(225), nullable=True)
    date = Column(String(225), nullable=True)
    date_time = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    status = Column(Integer, nullable=False, default=0)
    
    orders = relationship("HouseOrders", back_populates="user")
    settings = relationship("HouseUserSettings", back_populates="houseuser")
    verification = relationship("OTPVerification", back_populates="houseuser")
    houseusersubscriptions = relationship("Subscription", back_populates="houseuser")
    customelementrequest = relationship("CustomizationRequest", back_populates="user")  # Corrected the relationship


class HouseOrders(Base):
    __tablename__ = "houseorders"

    oid = Column(Integer, primary_key=True, autoincrement=True)
    id = Column(Integer, ForeignKey('houseuser.id'), nullable=True) 
    pid = Column(Integer, ForeignKey('price.pid'),nullable=False)
    date = Column(Date, nullable=True)
    status = Column(Integer, nullable=False, default=0)
    datetime = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    
    user = relationship("Houseuser", back_populates="orders")
    price = relationship("Price", back_populates="orders")


class Price(Base):
    __tablename__ = "price"

    pid = Column(Integer, primary_key=True, autoincrement=True)
    poid = Column(Integer, ForeignKey('houseproducts.poid'), nullable=False)  
    amount = Column(String(225), nullable=True)  
    name = Column(String(225), nullable=True)  
    status = Column(Integer, nullable=False, default=0) 
    datetime = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False) 
    description = Column(String(225), nullable=True)  
    key = Column(String(225), nullable=True)  

    orders = relationship("HouseOrders", back_populates="price")
    products = relationship("HouseProducts", back_populates="price")

class HouseProducts(Base):
    __tablename__ = "houseproducts"

    poid = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(225), nullable=True)
    description = Column(String(225), nullable=True)
    datetime = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    status = Column(Integer, nullable=False, default=0)
    category = Column(String(225), nullable=True)
    image = Column(String(225), nullable=True)
    planscheme_id = Column(Integer, nullable=True)

    price = relationship("Price", back_populates="products")
    feature = relationship("HouseProductsFeature", back_populates="productfeature")
    technical = relationship("HouseProductsTechnical", back_populates="producttechnical")
    compatibility = relationship("HouseProductsCompatibility", back_populates="productcompatibility")
    houseusersubscriptions = relationship("Subscription", back_populates="products")
    productimages = relationship("HouseImages", back_populates="products")
    productdeviceimages = relationship("HouseDeviceImages", back_populates="products")
    productoffers = relationship("HouseOffers", back_populates="products")
    productcustomelements = relationship("HouseProductCustomelements", back_populates="products")
    customelementrequest = relationship("CustomizationRequest", back_populates="products")


class HouseProductsFeature(Base):  
    __tablename__ = "houseproductfeature"  

    fid = Column(Integer, primary_key=True, autoincrement=True)
    poid = Column(Integer, ForeignKey('houseproducts.poid'), nullable=False)
    name = Column(String(225), nullable=False)
    status = Column(Integer, nullable=False, default=0)
    datetime = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)

    productfeature = relationship("HouseProducts", back_populates="feature")

class HouseProductsCompatibility(Base):  
    __tablename__ = "houseproductcompatibility"  

    cid = Column(Integer, primary_key=True, autoincrement=True)
    poid = Column(Integer, ForeignKey('houseproducts.poid'), nullable=False)
    name = Column(String(225), nullable=False)
    status = Column(Integer, nullable=False, default=0)
    datetime = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)

    productcompatibility = relationship("HouseProducts", back_populates="compatibility")

class HouseProductsTechnical(Base):  
    __tablename__ = "houseproducttechnical"  

    tid = Column(Integer, primary_key=True, autoincrement=True)
    poid = Column(Integer, ForeignKey('houseproducts.poid'), nullable=False)
    name = Column(String(225), nullable=False)
    status = Column(Integer, nullable=False, default=0)
    datetime = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)

    producttechnical = relationship("HouseProducts", back_populates="technical")

class HouseUserSettings(Base):  
    __tablename__ = "houseusersettings"  

    sid = Column(Integer, primary_key=True, autoincrement=True)
    field = Column(String(225), nullable=False)
    value = Column(String(225), nullable=False)
    id = Column(Integer, ForeignKey('houseuser.id'), nullable=False)
    datetime = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)

    houseuser = relationship("Houseuser", back_populates="settings")

class OTPVerification(Base):
    __tablename__ = "otp_verification"
    oid = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(225), nullable=False)
    otp = Column(String(225), nullable=False)
    expires_at = Column(DateTime, nullable=False)
    id = Column(Integer, ForeignKey('houseuser.id'), nullable=False)

    houseuser = relationship("Houseuser", back_populates="verification")

class Subscription(Base):
    __tablename__ = "subscriptions"

    suid = Column(Integer, primary_key=True, autoincrement=True)
    id = Column(Integer, ForeignKey('houseuser.id'), nullable=False)
    poid = Column(Integer, ForeignKey('houseproducts.poid'), nullable=False)
    plan_name = Column(String(225), nullable=False)
    amount = Column(Float, nullable=False)
    payment_method = Column(String(225), nullable=False)
    type_payment = Column(String(225), nullable=True)
    status = Column(String(225), nullable=False)
    billing_cycle = Column(String(225), nullable=False)  # monthly, quarterly, annually
    billing_date = Column(DateTime, nullable=False)
    expiration_date = Column(DateTime, nullable=False)
    current_price = Column(Float, nullable=False)
    selected_features = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)

    houseuser = relationship("Houseuser", back_populates="houseusersubscriptions")
    products = relationship("HouseProducts", back_populates="houseusersubscriptions")

class HouseImages(Base):  
    __tablename__ = "houseimages"  

    imd = Column(Integer, primary_key=True, autoincrement=True)
    poid = Column(Integer, ForeignKey('houseproducts.poid'), nullable=False)
    images = Column(String(225), nullable=False)
    datetime = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)

    products = relationship("HouseProducts", back_populates="productimages")

class HouseOffers(Base):  
    __tablename__ = "houseoffers"  

    oid = Column(Integer, primary_key=True, autoincrement=True)
    poid = Column(Integer, ForeignKey('houseproducts.poid'), nullable=False)
    discountpercentage = Column(String(225), nullable=False)
    startdate = Column(String(225), nullable=False)
    enddate = Column(String(225), nullable=False)
    datetime = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    status = Column(Integer, nullable=False, default=0)

    products = relationship("HouseProducts", back_populates="productoffers")


class PlanModel(Base):
    __tablename__ = "plans"
    pid = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    base_price = Column(Float, nullable=False)
    description = Column(String, nullable=True)
    planscheme_id = Column(Integer, nullable=False)
    includedFeatures = Column(String, nullable=True)

    features = relationship("FeatureModel", back_populates="plan")

class FeatureModel(Base):
    __tablename__ = "features"
    feid = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    plan_id = Column(Integer, ForeignKey("plans.pid"),nullable=True)
    
    plan = relationship("PlanModel", back_populates="features")


class HouseDeviceImages(Base):  
    __tablename__ = "housedeviceimages"  

    dimd = Column(Integer, primary_key=True, autoincrement=True)
    poid = Column(Integer, ForeignKey('houseproducts.poid'), nullable=False)
    device_name = Column(String(225), nullable=False)
    image_url = Column(String(225), nullable=False)

    products = relationship("HouseProducts", back_populates="productdeviceimages")

class HouseProductCustomelements(Base):  
    __tablename__ = "houseproductcustomelements"  

    cpid = Column(Integer, primary_key=True, autoincrement=True)
    poid = Column(Integer, ForeignKey('houseproducts.poid'), nullable=False)
    name = Column(String(225), nullable=False)
    description = Column(String(225), nullable=False)

    products = relationship("HouseProducts", back_populates="productcustomelements")


class CustomizationRequest(Base):
    __tablename__ = "customizationrequest"

    rid = Column(Integer, primary_key=True, autoincrement=True)
    poid = Column(Integer, ForeignKey('houseproducts.poid'), nullable=False)
    id = Column(Integer, ForeignKey('houseuser.id'), nullable=True) 
    name = Column(String(225), nullable=False) 
    customize = Column(String(225), nullable=False) 
    status = Column(Integer, nullable=False, default=0) 
    datetime = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False) 

    products = relationship("HouseProducts", back_populates="customelementrequest")
    user = relationship("Houseuser", back_populates="customelementrequest")  # Corrected the relationship

