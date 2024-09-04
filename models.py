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
    id = Column(Integer, ForeignKey('houseuser.id'), nullable=True)  # Foreign key referencing Houseuser.id
    pid = Column(Integer, ForeignKey('price.pid'),nullable=False)
    date = Column(Date, nullable=True)
    status = Column(Integer, nullable=False, default=0)
    datetime = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    
    user = relationship("Houseuser", back_populates="orders")
    price = relationship("Price", back_populates="orders")


class Price(Base):
    __tablename__ = "price"

    pid = Column(Integer, primary_key=True, autoincrement=True)  # Primary key, auto-increment
    amount = Column(String(225), nullable=True)  # Amount as varchar(225)
    name = Column(String(225), nullable=True)  # Name as varchar(225)
    status = Column(Integer, nullable=False, default=0)  # Status, default is 0
    datetime = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)  # Timestamp, default is current timestamp
    description = Column(String(225), nullable=True)  # Description as varchar(225)
    key = Column(String(225), nullable=True)  # Key as varchar(225)

    # Define the reverse relationship to HouseOrders
    orders = relationship("HouseOrders", back_populates="price")