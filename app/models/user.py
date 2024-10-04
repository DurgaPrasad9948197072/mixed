from sqlalchemy import Column, Integer, String, TIMESTAMP, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

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

    price = relationship("Price", back_populates="products")
    feature = relationship("HouseProductsFeature", back_populates="productfeature")
    technical = relationship("HouseProductsTechnical", back_populates="producttechnical")
    compatibility = relationship("HouseProductsCompatibility", back_populates="productcompatibility")


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