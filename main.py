from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.orm import Session
from database import get_db  
# from schemas import RegisterHouseRequest,LoginHouseRequest,UpdateHouseUserRequest,HouseOrderRequest,CreatePriceRequest  
# from models import Houseuser, HouseOrders ,Price
from app.routers.user import user
app = FastAPI()

# Define a list of origins that should be permitted to make cross-origin requests.
origins = [
    "http://localhost:3000",
    "http://localhost:4200",  
    "https://www.example.com",
]

# Add middleware to allow cross-origin requests from the specified origins.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows specified origins to make requests.
    allow_credentials=True,  # Allows credentials to be submitted with a cross-origin request.
    allow_methods=["*"],  # Allows all HTTP methods.
    allow_headers=["*"],  # Allows all headers.
)

app.include_router(user, tags=["User"], prefix="/user")


@app.get("/")
async def main():
    return {"message": "Hello World"}

# @app.post("/house_login")
# async def login(login_request: LoginHouseRequest, db: Session = Depends(get_db)):
#     user = db.query(Houseuser).filter_by(email=login_request.email, password=login_request.password).first()
    
#     if user is None:
#         return {"result": "error", "message": "User not found"}

#     return {
#         "result": "success",
#         "message": "Login successful",
#         "data": {
#             "id": user.id,
#             "email": user.email,
#             "date": user.date,
#             "status": user.status
#         }
#     }

# @app.post("/house_reg/")
# async def register_user(request: RegisterHouseRequest, db: Session = Depends(get_db)):
#     existing_user = db.query(Houseuser).filter_by(email=request.email).first()
#     if existing_user:
#         return {"result": "error", "message": "User already exists"}
    
#     new_user = Houseuser(
#         email=request.email,
#         password=request.password,
#         username=request.username,
#         date=datetime.now().strftime('%Y-%m-%d'),
#         status=0 
#     )
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
    
#     return {
#         "result": "success",
#         "message": "User registered successfully",
#         "data": {
#             "id": new_user.id,
#             "email": new_user.email,
#             "date": new_user.date,
#             "status": new_user.status
#         }
#     }


# @app.put("/update-house_user/{user_id}")
# async def update_user(user_id: int, request: UpdateHouseUserRequest, db: Session = Depends(get_db)):
#     user = db.query(Houseuser).filter_by(id=user_id).first()
    
#     if user is None:
#         return {"result": "error", "message": "User not found"}
    
#     if request.email:
#         user.email = request.email
#     if request.password:
#         user.password = request.password
#     if request.status is not None:
#         user.status = request.status
    
#     db.commit()
#     db.refresh(user)
    
#     return {
#         "result": "success",
#         "message": "User updated successfully",
#         "data": {
#             "id": user.id,
#             "email": user.email,
#             "status": user.status,
#             "date": user.date
#         }
#     }



# @app.post("/create-order/")
# async def create_order(order_request: HouseOrderRequest, db: Session = Depends(get_db)):
#     new_order = HouseOrders(
#         id=order_request.id,
#         pid=order_request.pid,
#         date=order_request.date if order_request.date else datetime.utcnow().date(),
#         status=order_request.status
#     )
#     db.add(new_order)
#     db.commit()
#     db.refresh(new_order)
    
#     return {
#         "result": "success",
#         "order": {
#             "oid": new_order.oid,
#             "id": new_order.id,
#             "pid": new_order.pid,
#             "date": new_order.date,
#             "status": new_order.status,
#             "datetime": new_order.datetime
#         }
#     }


# @app.get("/house_order/{oid}/user")
# async def get_user_by_order(oid: int, db: Session = Depends(get_db)):
#     order = db.query(HouseOrders).filter(HouseOrders.oid == oid).first()

#     if not order:
#         raise HTTPException(status_code=404, detail="Order not found")

#     user = order.user

#     if not user:
#         raise HTTPException(status_code=404, detail="User not found for this order")

#     return {
#         "id": user.id,
#         "email": user.email,
#         "status": user.status,
#         "date_time": user.date_time,
#         "orders": len(user.orders)  
#     }


# @app.get("/order/{oid}")
# async def get_order_details(oid: int, db: Session = Depends(get_db)):
#     order = db.query(HouseOrders).filter(HouseOrders.oid == oid).first()

#     if not order:
#         raise HTTPException(status_code=404, detail="Order not found")

#     price = order.price

#     return {
#         "oid": order.oid,
#         "user_id": order.id,
#         "price_id": price.pid,
#         "price_name": price.name,
#         "price_amount": price.amount,
#         "order_status": order.status,
#         "price_status": price.status,
#         "order_datetime": order.datetime,
#         "price_description": price.description
#     }


# @app.post("/create-price/")
# async def create_price(price_request: CreatePriceRequest, db: Session = Depends(get_db)):
#     new_price = Price(
#         amount=price_request.amount,
#         name=price_request.name,
#         status=price_request.status,
#         description=price_request.description,
#         key=price_request.key
#     )
#     db.add(new_price)
#     db.commit()
#     db.refresh(new_price)
    
#     return {
#         "result": "success",
#         "price": {
#             "pid": new_price.pid,
#             "amount": new_price.amount,
#             "name": new_price.name,
#             "status": new_price.status,
#             "description": new_price.description,
#             "key": new_price.key,
#             "datetime": new_price.datetime
#         }
#     }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
