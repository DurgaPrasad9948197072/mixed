from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from database import get_db
from app.schemas.user import RegisterHouseRequest,LoginHouseRequest,UpdateHouseUserRequest,HouseOrderRequest,CreatePriceRequest,ProductHouseRequest 
from app.models.user import Houseuser,HouseOrders,Price,HouseProducts,HouseProductsFeature,HouseProductsTechnical,HouseProductsCompatibility
from datetime import datetime

user = APIRouter()

@user.post("/house_login/")
async def login(login_request: LoginHouseRequest, db: Session = Depends(get_db)):
    user = db.query(Houseuser).filter_by(email=login_request.email, password=login_request.password).first()
    
    if user is None:
        return {"result": "error", "message": "User not found"}

    return {
        "result": "success",
        "message": "Login successful",
        "data": {
            "id": user.id,
            "email": user.email,
            "date": user.date,
            "status": user.status
        }
    }

@user.post("/house_reg/")
async def register_user(request: RegisterHouseRequest, db: Session = Depends(get_db)):
    existing_user = db.query(Houseuser).filter_by(email=request.email).first()
    if existing_user:
        return {"result": "error", "message": "User already exists"}
    
    new_user = Houseuser(
        email=request.email,
        password=request.password,
        username=request.username,
        date=datetime.now().strftime('%Y-%m-%d'),
        status=0 
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {
        "result": "success",
        "message": "User registered successfully",
        "data": {
            "id": new_user.id,
            "email": new_user.email,
            "date": new_user.date,
            "status": new_user.status
        }
    }


@user.put("/update-house_user/{user_id}")
async def update_user(user_id: int, request: UpdateHouseUserRequest, db: Session = Depends(get_db)):
    user = db.query(Houseuser).filter_by(id=user_id).first()
    
    if user is None:
        return {"result": "error", "message": "User not found"}
    
    if request.email:
        user.email = request.email
    if request.password:
        user.password = request.password
    if request.status is not None:
        user.status = request.status
    
    db.commit()
    db.refresh(user)
    
    return {
        "result": "success",
        "message": "User updated successfully",
        "data": {
            "id": user.id,
            "email": user.email,
            "status": user.status,
            "date": user.date
        }
    }


@user.post("/create-order/")
async def create_order(order_request: HouseOrderRequest, db: Session = Depends(get_db)):
    new_order = HouseOrders(
        id=order_request.id,
        pid=order_request.pid,
        date=order_request.date if order_request.date else datetime.utcnow().date(),
        status=order_request.status
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    
    return {
        "result": "success",
        "order": {
            "oid": new_order.oid,
            "id": new_order.id,
            "pid": new_order.pid,
            "date": new_order.date,
            "status": new_order.status,
            "datetime": new_order.datetime
        }
    }


@user.get("/house_order/{oid}/user")
async def get_user_by_order(oid: int, db: Session = Depends(get_db)):
    order = db.query(HouseOrders).filter(HouseOrders.oid == oid).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    user = order.user

    if not user:
        raise HTTPException(status_code=404, detail="User not found for this order")

    return {
        "id": user.id,
        "email": user.email,
        "status": user.status,
        "date_time": user.date_time,
        "orders": len(user.orders)  
    }


@user.get("/order/{oid}")
async def get_order_details(oid: int, db: Session = Depends(get_db)):
    order = db.query(HouseOrders).filter(HouseOrders.oid == oid).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    price = order.price

    return {
        "oid": order.oid,
        "user_id": order.id,
        "price_id": price.pid,
        "price_name": price.name,
        "price_amount": price.amount,
        "order_status": order.status,
        "price_status": price.status,
        "order_datetime": order.datetime,
        "price_description": price.description
    }


@user.post("/create-price/")
async def create_price(price_request: CreatePriceRequest, db: Session = Depends(get_db)):
    new_price = Price(
        amount=price_request.amount,
        name=price_request.name,
        status=price_request.status,
        description=price_request.description,
        key=price_request.key
    )
    db.add(new_price)
    db.commit()
    db.refresh(new_price)
    
    return {
        "result": "success",
        "price": {
            "pid": new_price.pid,
            "amount": new_price.amount,
            "name": new_price.name,
            "status": new_price.status,
            "description": new_price.description,
            "key": new_price.key,
            "datetime": new_price.datetime
        }
    }

@user.post("/house_product/")
async def insert_products(request: ProductHouseRequest, db: Session = Depends(get_db)):
    existing_product = db.query(HouseProducts).filter_by(name=request.name).first()
    if existing_product:
        return {"result": "error", "message": "Product already exists"}
    
    new_product = HouseProducts(
        name=request.name,
        description=request.description,
        category=request.category,
        image=request.image,
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    if request.price:
        new_price = Price(
            poid=new_product.poid,  
            amount=request.price.amount,
            name=request.price.name,
            description=request.price.description,
            key=request.price.key,
            status=request.price.status
        )
        db.add(new_price)
    
    if request.features:
        for feature in request.features:
            new_feature = HouseProductsFeature(
                poid=new_product.poid,
                name=feature.name,
                status=feature.status,
            )
            db.add(new_feature)

    if request.technical:
        for technical in request.technical:
            new_technical = HouseProductsTechnical(
                poid=new_product.poid,
                name=technical.name,
                status=technical.status,
            )
            db.add(new_technical)

    if request.compatibility:
        for compatibility in request.compatibility:
            new_compatibility = HouseProductsCompatibility(
                poid=new_product.poid,
                name=compatibility.name,
                status=compatibility.status,
            )
            db.add(new_compatibility)

    db.commit()

    return {
        "result": "success",
        "message": "Product registered successfully",
        "data": {
            "poid": new_product.poid,
            "name": new_product.name,
            "date": new_product.datetime,
            "status": new_product.status
        }
    }

@user.get("/house_product_getdeatils/{product_id}")
async def get_product_details(product_id: int, db: Session = Depends(get_db)):
    product = db.query(HouseProducts).filter_by(poid=product_id).first()
    if not product:
        return {"result": "error", "message": "Product not found"}
    
    features = db.query(HouseProductsFeature).filter_by(poid=product.poid).all()
    technicals = db.query(HouseProductsTechnical).filter_by(poid=product.poid).all()
    compatibilities = db.query(HouseProductsCompatibility).filter_by(poid=product.poid).first()
    price = db.query(Price).filter_by(poid=product.poid).first()

    response = {
        "result": "success",
        "data": {
            "poid": product.poid,
            "image": product.image,
            "name": product.name,
            "description": product.description,
            "datetime": product.datetime,
            "status": product.status,
            "price": price.amount,
            "features": [ f.name for f in features],
            "technical": [ t.name for t in technicals],
            "compatibility": compatibilities.name
        }
    }

    return response

@user.get("/house_product_list/")
async def get_product_list(db: Session = Depends(get_db)):
    products = db.query(HouseProducts).filter_by(status=0).all()
    if not products:
        return {"result": "error", "message": "No products found"}
    
    product_list = []
    for product in products:
        price = db.query(Price).filter_by(poid=product.poid).first()

        product_data = {
            "id": product.poid,
            "name": product.name,
            "image": product.image,
            "category": product.category,
            "description": product.description,
            "datetime": product.datetime,
            "status": product.status,
            "price": price.amount,
        }
        
        product_list.append(product_data)

    return {
        "result": "success",
        "data": product_list
    }
