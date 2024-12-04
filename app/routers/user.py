from fastapi import APIRouter, Depends, Form, File, UploadFile, Body, HTTPException
from typing import List,Union
from sqlalchemy.orm import Session
from app import models, schemas
from database import get_db
from app.schemas.user import RegisterHouseRequest,LoginHouseRequest,UpdateHouseUserRequest,HouseOrderRequest,CreatePriceRequest,ProductHouseRequest,UpdateHouseSettingsRequest,OTPRequest,OTPVerify,SearchQuery,CreateSubscriptionRequest,UpdateProductHouseRequest,ImageDeletionResponse ,OfferCreate, OfferUpdate, OfferResponse, ReviewRequest, EmailRequest,Feature,Plan,FeaturesRequest,CustomizationRequestPayload,CustomizationGroup,CustomizationRequestResponse,UserDetails,ProductDetails,UpdateCustomizationStatusRequest
from app.models.user import Houseuser,HouseOrders,Price,HouseProducts,HouseProductsFeature,HouseProductsTechnical,HouseProductsCompatibility,HouseUserSettings,OTPVerification,Subscription,HouseImages,HouseOffers,PlanModel,FeatureModel,HouseDeviceImages,HouseProductCustomelements,CustomizationRequest
from datetime import datetime, timedelta
from aiosmtplib import SMTP
from email.message import EmailMessage
import random
from datetime import datetime, timedelta
from app.utlity.outer_api import upload_image_to_imgbb
from app.utlity.mailer import send_email_support
from io import BytesIO
import json

user = APIRouter()

@user.post("/house_login/")
async def login(login_request: LoginHouseRequest, db: Session = Depends(get_db)):
    user = db.query(Houseuser).filter_by(email=login_request.email, password=login_request.password).first()

    if user is None:
        return {"result": "error", "message": "User not found"}
    settings = db.query(HouseUserSettings).filter_by(id=user.id).all()

    settings_data = {}
    for setting in settings:
        settings_data[setting.field] = setting.value
     
    return {
        "result": "success",
        "message": "Login successful",
        "data": {
            "id": user.id,
            "email": user.email,
            "date": user.date,
            "settings": settings_data, 
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
    settings = db.query(HouseUserSettings).filter_by(id=user_id).all()

    if user is None:
        return {"result": "error", "message": "User not found"}

    if request.username:
        user.username = request.username
    if request.email:
        user.email = request.email
    if request.password:
        user.password = request.password
    if request.status is not None:
        user.status = request.status
    
    db.commit()
    db.refresh(user)
    

    settings_data = {}
    for setting in settings:
        settings_data[setting.field] = setting.value
        
    return {
        "result": "success",
        "message": "User updated successfully",
        "data": {
            "id": user.id,
            "email": user.email,
            "username": user.username,
            "status": user.status,
            "date": user.date,
            "settings": settings_data 

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
async def create_product(
    data: str = Form(...),  # JSON payload as a string
    file: UploadFile = File(None),  # Optional file upload
    db: Session = Depends(get_db),
):
    # Parse JSON data
    product_data = json.loads(data)

    # Upload the file to ImgBB if provided
    image_url = None
    if file:
        image_url = await upload_image_to_imgbb(file)

    # Create a new product entry
    new_product = HouseProducts(
        name=product_data["name"],
        description=product_data["description"],
        category=product_data["category"],
        planscheme_id=product_data["planscheme_id"],
        image=image_url,  # Save the ImgBB URL
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    if "features" in product_data:
        for feature in product_data["features"]:
            new_feature = HouseProductsFeature(
                poid=new_product.poid,
                name=feature["name"],
                status=feature.get("status", 1),  # Default status to 1
            )
            db.add(new_feature)

    if "technical" in product_data:
        for tech in product_data["technical"]:
            new_technical = HouseProductsTechnical(
                poid=new_product.poid,
                name=tech["name"],
                status=tech.get("status", 1),
            )
            db.add(new_technical)

    if "compatibility" in product_data:
        for comp in product_data["compatibility"]:
            new_compatibility = HouseProductsCompatibility(
                poid=new_product.poid,
                name=comp["name"],
                status=comp.get("status", 1),
            )
            db.add(new_compatibility)

    if "customElements" in product_data:
        for customElements in product_data["customElements"]:
            new_customElements = HouseProductCustomelements(
                poid=new_product.poid,
                name=customElements["name"],
                description=customElements["description"],
            )
            db.add(new_customElements)

    db.commit()

    return {
        "result": "success",
        "message": "Product created successfully",
        "data": {
            "poid": new_product.poid,
            "name": new_product.name,
            "date": new_product.datetime,
            "status": new_product.status,
            "image": new_product.image,
        },
    }

@user.put("/house_update_product/{product_id}")
async def update_product(
    product_id: int,
    data: str = Form(...),  # JSON payload as a string
    file: UploadFile = File(None),  # Optional file upload
    db: Session = Depends(get_db),
):
    # Parse JSON data
    product_data = json.loads(data)

    # Fetch the existing product by product_id
    product = db.query(HouseProducts).filter_by(poid=product_id).first()
    if not product:
        return {"result": "error", "message": "Product not found"}

    # Update basic product details
    product.name = product_data["name"]
    product.category = product_data["category"]
    product.description = product_data["description"]
    product.planscheme_id=product_data["planscheme_id"],

    # If a new file is uploaded, update the image field with the new URL
    if file:
        image_url = await upload_image_to_imgbb(file)  # Use the ImgBB uploader defined earlier
        product.image = image_url

    db.commit()
    db.refresh(product)

    # Update features
    db.query(HouseProductsFeature).filter_by(poid=product_id).delete()  # Clear existing features
    if "features" in product_data:
        for feature in product_data["features"]:
            new_feature = HouseProductsFeature(
                poid=product_id,
                name=feature["name"],
            )
            db.add(new_feature)

    # Update technical specifications
    db.query(HouseProductsTechnical).filter_by(poid=product_id).delete()  # Clear existing technical specs
    if "technical" in product_data:
        for technical in product_data["technical"]:
            new_technical = HouseProductsTechnical(
                poid=product_id,
                name=technical["name"],
            )
            db.add(new_technical)

    # Update compatibility
    db.query(HouseProductsCompatibility).filter_by(poid=product_id).delete()  # Clear existing compatibility info
    if "compatibility" in product_data:
        for compatibility in product_data["compatibility"]:
            new_compatibility = HouseProductsCompatibility(
                poid=product_id,
                name=compatibility["name"],
            )
            db.add(new_compatibility)

    # Update customElements
    db.query(HouseProductCustomelements).filter_by(poid=product_id).delete()  # Clear existing compatibility info
    if "customElements" in product_data:
        for customElements in product_data["customElements"]:
            new_customElements = HouseProductCustomelements(
                poid=product_id,
                name=customElements["name"],
                description=customElements["description"],
            )
            db.add(new_customElements)

    db.commit()

    return {
        "result": "success",
        "message": "Product updated successfully",
        "data": {
            "poid": product.poid,
            "name": product.name,
            "date": product.datetime,
            "status": product.status,
        },
    }

    
@user.get("/house_product_getdeatils/{product_id}")
async def get_product_details(product_id: int, db: Session = Depends(get_db)):
    product = db.query(HouseProducts).filter_by(poid=product_id).first()
    if not product:
        return {"result": "error", "message": "Product not found"}
    
    features = db.query(HouseProductsFeature).filter_by(poid=product.poid).all()
    technicals = db.query(HouseProductsTechnical).filter_by(poid=product.poid).all()
    compatibilities = db.query(HouseProductsCompatibility).filter_by(poid=product.poid).first()
    # price = db.query(Price).filter_by(poid=product.poid).first()
    images = db.query(HouseImages).filter_by(poid=product.poid).all()
    offer = db.query(HouseOffers).filter_by(poid = product.poid).first()
    # Fetch the first plan associated with the product's planscheme_id
    plan = db.query(PlanModel).filter(PlanModel.planscheme_id == product.planscheme_id).first()
    plan_name = plan.name if plan else "N/A"
    base_price = plan.base_price if plan else "N/A"

    # Calculate the total feature price for the same planscheme_id
    feature_prices = db.query(FeatureModel).filter(
        FeatureModel.plan_id == product.planscheme_id
    ).all()
    total_feature_price = sum(f.price for f in feature_prices) if feature_prices else 0

    # Replace the price with the sum of the base price and total feature price
    combined_price = base_price + total_feature_price if base_price != "N/A" else "N/A"
    response = {
        "result": "success",
        "data": {
            "id": product.poid,
            "images": [ i.images for i in images],            
            "image": product.image,
            "planscheme_id" : product.planscheme_id,
            "name": product.name,
            "description": product.description,
            "rating": 5,
            "sales": 396,
            "category": product.category,
            "datetime": product.datetime,
            "status": product.status,
            "originalPrice": 22.00,
            "price": combined_price,
            "tags": ["Beauty", "Salon", "Next.js", "Responsive"],
            "lastUpdate": product.datetime,
            "version": "1.1.0",
            "features": [ f.name for f in features],
            "compatibleBrowsers": [ t.name for t in technicals],
            "offer": {
                "id": offer.oid,
                "discountPercentage": offer.discountpercentage,
                "startDate": offer.startdate,
                "endDate": offer.enddate,
             } if offer else None,
            "plan_name": plan_name,
        }
    }

    return response


@user.get("/house_product_list/")
async def get_product_list(db: Session = Depends(get_db)):
    # Query products that are active (status = 1) and not subscribed (poid not in subscriptions)
    products = db.query(HouseProducts).filter(
        HouseProducts.status == 1,
        ~HouseProducts.poid.in_(
            db.query(Subscription.poid).filter(Subscription.status == "active")
        )
    ).all()

    if not products:
        return {"result": "error", "message": "No available products found"}

    product_list = []
    for product in products:
        # Fetch the price for each product
        # price = db.query(Price).filter_by(poid=product.poid).first()
        features = db.query(HouseProductsFeature).filter_by(poid=product.poid).all()
        technicals = db.query(HouseProductsTechnical).filter_by(poid=product.poid).all()
        images = db.query(HouseImages).filter_by(poid=product.poid).all()
        offer = db.query(HouseOffers).filter_by(poid=product.poid).first()
        
        # Fetch the first plan associated with the product's planscheme_id
        plan = db.query(PlanModel).filter(PlanModel.planscheme_id == product.planscheme_id).first()
        plan_name = plan.name if plan else "N/A"
        base_price = plan.base_price if plan else "N/A"

        # Calculate the total feature price for the same planscheme_id
        feature_prices = db.query(FeatureModel).filter(
            FeatureModel.plan_id == product.planscheme_id
        ).all()
        total_feature_price = sum(f.price for f in feature_prices) if feature_prices else 0

        # Replace the price with the sum of the base price and total feature price
        combined_price = base_price + total_feature_price if base_price != "N/A" else "N/A"
        if combined_price is "N/A":
            continue
        product_data = {
            "id": product.poid,
            "name": product.name,
            "images": [i.images for i in images],
            "image": product.image,
            "planscheme_id": product.planscheme_id,
            "category": product.category,
            "description": product.description,
            "datetime": product.datetime,
            "status": product.status,
            "price": combined_price,
            "originalPrice": 22.00,  # Replace with actual price logic if needed
            "rating": 5,  # Replace with actual rating logic if needed
            "sales": 396,  # Replace with actual sales logic if needed
            "features": [f.name for f in features],
            "technical": [t.name for t in technicals],
            "offer": {
                "id": offer.oid,
                "discountPercentage": offer.discountpercentage,
                "startDate": offer.startdate,
                "endDate": offer.enddate,
            } if offer else None,
            "plan_name": plan_name,
        }
        
        product_list.append(product_data)

    return {
        "result": "success",
        "data": product_list
    }

@user.get("/house_product_list_with_image_count/")
async def get_product_list(db: Session = Depends(get_db)):
    """
    Fetch a list of available house products along with their associated images,
    features, technical details, and device-specific images.
    """
    # Query products that are active (status = 0) and not subscribed (poid not in subscriptions)
    products = db.query(HouseProducts).filter(
        ~HouseProducts.poid.in_(
            db.query(Subscription.poid).filter(Subscription.status == "active")
        )
    ).all()

    if not products:
        return {"result": "error", "message": "No available products found"}

    product_list = []
    for product in products:
        # Fetch product details
        price = db.query(Price).filter_by(poid=product.poid).first()
        features = db.query(HouseProductsFeature).filter_by(poid=product.poid).all()
        technicals = db.query(HouseProductsTechnical).filter_by(poid=product.poid).all()
        images = db.query(HouseImages).filter_by(poid=product.poid).all()
        device_images = db.query(HouseDeviceImages).filter_by(poid=product.poid).all()
        image_count = db.query(HouseImages).filter_by(poid=product.poid).count()

        # Prepare image data
        image_data = [{"imd": image.imd, "image_url": image.images} for image in images]

        # Prepare device image data
        device_image_data = [
            {
                "dimd": device_image.dimd,
                "device_name": device_image.device_name,
                "image_url": device_image.image_url,
            }
            for device_image in device_images
        ]

        # Compile product data
        product_data = {
            "id": product.poid,
            "name": product.name,
            "image": product.image,
            "category": product.category,
            "description": product.description,
            "datetime": product.datetime,
            "status": product.status,
            "price": price.amount if price else "N/A",  # Handle missing price
            "originalPrice": 22.00,  # Placeholder for original price logic
            "rating": 5,  # Placeholder for rating logic
            "sales": 396,  # Placeholder for sales data
            "features": [f.name for f in features],
            "technical": [t.name for t in technicals],
            "images": image_data,
            "device_images": device_image_data,
            "imageCount": image_count,
        }

        product_list.append(product_data)

    return {
        "result": "success",
        "data": product_list,
    }


@user.put("/update-house-settings/{user_id}")
async def update_house_settings(
    user_id: int,
    request: UpdateHouseSettingsRequest,
    db: Session = Depends(get_db),
):
    user = db.query(Houseuser).filter(Houseuser.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    setting = (
        db.query(HouseUserSettings)
        .filter(
            HouseUserSettings.id == request.uid,
            HouseUserSettings.field == request.field,
        )
        .first()
    )

    if setting:
        setting.value = request.value
    else:
        new_setting = HouseUserSettings(
            id=request.uid,
            field=request.field,
            value=request.value,
        )
        db.add(new_setting)

    db.commit()

    return {
        "result": "success",
        "message": "House settings updated successfully",
    }

# async def send_email(email: str, otp: str):
#     message = EmailMessage()
#     message["From"] = "testgo@gmail.com"
#     message["To"] = email
#     message["Subject"] = "Your OTP Code"
#     message.set_content(f"Your OTP code is {otp}. It expires in 10 minutes.")
    
#     async with SMTP("smtp.gmail.com", port=587) as smtp:
#         await smtp.starttls()
#         await smtp.login("your-email@example.com", "your-password")
#         await smtp.send_message(message)


@user.post("/generate-otp")
async def generate_otp_endpoint(request: OTPRequest, db: Session = Depends(get_db)):
    otp = random.randint(100000, 999999)
    expires_at = datetime.utcnow() + timedelta(minutes=10)

    otp_entry = db.query(OTPVerification).filter_by(id=request.id).first()
    if otp_entry:
        otp_entry.otp = otp
        otp_entry.expires_at = expires_at
    else:
        otp_entry = OTPVerification(id=request.id, email=request.email, otp=otp, expires_at=expires_at)
        db.add(otp_entry)

    db.commit()
    # await send_email(request.email, otp)
    return {
        "result": "success",
        "message": "OTP sent successfully",
    }


@user.post("/verify-otp")
def verify_otp_endpoint(request: OTPVerify, db: Session = Depends(get_db)):
    otp_entry = db.query(OTPVerification).filter_by(id=request.id).first()
    if not otp_entry:
        raise HTTPException(status_code=404, detail="OTP not found")

    if otp_entry.otp != request.otp:
        raise HTTPException(status_code=400, detail="Invalid OTP")

    if otp_entry.expires_at < datetime.utcnow():
        raise HTTPException(status_code=400, detail="OTP expired")

    # OTP is valid
    return {
        "result": "success",
        "message": "OTP verified successfully",
    }


async def send_email(email: str, otp: str):
    message = EmailMessage()
    message["From"] = "your-email@example.com"
    message["To"] = email
    message["Subject"] = "Your OTP Code"
    message.set_content(f"Your OTP code is {otp}. It expires in 10 minutes.")
    
    async with SMTP("smtp.gmail.com", port=587) as smtp:
        await smtp.starttls()
        await smtp.login("your-email@example.com", "your-password")
        await smtp.send_message(message)


@user.post("/search_product")
async def search_product(request: SearchQuery, db: Session = Depends(get_db)):
    # Start the query with active products
    query = db.query(HouseProducts).filter(
        HouseProducts.status == 0,
        ~HouseProducts.poid.in_(
            db.query(Subscription.poid).filter(Subscription.status == "active")
        )  # Exclude subscribed products
    )

    # Apply filters dynamically based on query parameters
    if request.name:
        query = query.filter(HouseProducts.name.ilike(f"%{request.name}%"))
    if request.category:
        query = query.filter(HouseProducts.category.ilike(f"%{request.category}%"))

    # Fetch all filtered products
    products = query.all()

    # If no products found, return an error
    if not products:
        return {"result": "error", "message": "No products found"}

    product_list = []
    for product in products:
        # Fetch product price
        price = db.query(Price).filter_by(poid=product.poid).first()

        # Check if price exists before accessing it
        product_price = price.amount if price else None

        product_data = {
            "id": product.poid,
            "name": product.name,
            "image": product.image,
            "category": product.category,
            "description": product.description,
            "datetime": product.datetime,
            "status": product.status,
            "price": product_price,
            "originalPrice": 22.00,  # Example static value, replace as needed
            "rating": 5,  # Example static value, replace as needed
            "sales": 396,  # Example static value, replace as needed
        }
        product_list.append(product_data)

    return {
        "result": "success",
        "data": product_list
    }

@user.post("/create_subscription/")
async def create_subscription(
    request: CreateSubscriptionRequest,
    db: Session = Depends(get_db)
):
    if request.billing_cycle not in ["monthly", "quarterly", "annually"]:
        return {"result": "error", "message": "Invalid billing cycle"}

    selectedfeatures = ",".join(map(str, request.selected_features)) if request.selected_features else None

    subscription = Subscription(
        id=request.user_id,
        poid=request.product_id,
        plan_name=request.plan_name,
        amount=request.amount,
        payment_method=request.payment_method,
        type_payment=request.type_payment,
        status=request.status,
        billing_cycle=request.billing_cycle,
        billing_date=request.billing_date,
        expiration_date=request.expiration_date,
        current_price=request.current_price,
        selected_features=selectedfeatures,
    )
    db.add(subscription)
    db.commit()
    db.refresh(subscription)

    return {
        "result": "success",
        "message": "Subscription created successfully",
        "data": {
            "subscription_id": subscription.suid,
            "user_id": subscription.id,
            "product_id": subscription.poid,
            "plan_name": subscription.plan_name,
            "amount": subscription.amount,
            "payment_method": subscription.payment_method,
            "status": subscription.status,
            "billing_cycle": subscription.billing_cycle,
            "billing_date": subscription.billing_date,
            "expiration_date": subscription.expiration_date,
            "current_price": subscription.current_price,
        },
    }


@user.get("/active_subscriptions/{user_id}/")
async def get_active_subscriptions(user_id: int, db: Session = Depends(get_db)):
    # Query only active subscriptions for the user
    subscriptions = db.query(Subscription).filter_by(id=user_id, status="active").all()
    
    # Handle case where no active subscriptions are found
    if not subscriptions:
        raise HTTPException(status_code=404, detail="No active subscriptions found for the user.")

    subscription_list = []

    for subscription in subscriptions:
        # Query the related product
        product = db.query(HouseProducts).filter_by(poid=subscription.poid).first()
        if not product:
            continue  # Skip if no product is found for the subscription

        # Ensure billing_date is a datetime object
        billing_date = subscription.billing_date if isinstance(subscription.billing_date, datetime) else datetime.strptime(str(subscription.billing_date), "%Y-%m-%d %H:%M:%S.%f")

        # Calculate nextBillingDate based on billing cycle
        next_billing_date = billing_date
        if subscription.billing_cycle == "monthly":
            next_billing_date += timedelta(days=30)
        elif subscription.billing_cycle == "quarterly":
            next_billing_date += timedelta(days=90)
        elif subscription.billing_cycle == "annually":
            next_billing_date += timedelta(days=365)

        # Prepare subscription data
        subscription_data = {
            "id": subscription.suid,
            "productName": product.name,
            "plan": subscription.plan_name,
            "price": subscription.current_price,
            "billingCycle": subscription.billing_cycle,
            "nextBillingDate": next_billing_date.date(),  # Extract date only
            "paymentMethod": subscription.payment_method,
        }

        subscription_list.append(subscription_data)

    return {
        "result": "success",
        "data": subscription_list
    }

@user.put("/cancel_subscription/{subscription_id}/")
async def cancel_subscription(subscription_id: int, db: Session = Depends(get_db)):
    # Fetch the subscription by id
    subscription = db.query(Subscription).filter_by(suid=subscription_id).first()

    # If the subscription doesn't exist
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found.")

    # If the subscription is already canceled
    if subscription.status == "canceled":
        raise HTTPException(status_code=400, detail="Subscription is already canceled.")

    # Update the subscription status to 'canceled'
    subscription.status = "canceled"
    subscription.updated_at = datetime.utcnow()  # Update the timestamp when canceled

    # Optionally, add a cancellation date if needed
    # subscription.canceled_at = datetime.utcnow()

    db.commit()  # Commit the transaction to the database
    db.refresh(subscription)  # Refresh the subscription to reflect the updated status

    return {"result": "success", "message": "Subscription has been successfully canceled."}

@user.post("/house_product_image_upload/")
async def upload_house_product_images(
    poid: int = Form(...),
    files: List[UploadFile] = File(...),  # Collect all files dynamically
    db: Session = Depends(get_db),
):
    if not poid:
        raise HTTPException(status_code=400, detail="Product ID (poid) is required")

    if not files or len(files) == 0:
        raise HTTPException(status_code=400, detail="No files provided for upload")

    # Process each file
    image_urls = []
    for file in files:
        # Upload image to ImgBB
        image_url = await upload_image_to_imgbb(file)
        image_urls.append(image_url)

        # Save image details in the database
        house_image = HouseImages(poid=poid, images=image_url)
        db.add(house_image)

    db.commit()

    return {"result": "success", "uploaded_urls": image_urls}


@user.post("/house_product_image_delete/")
async def delete_image(poid: int, imd: int, db: Session = Depends(get_db)):
    # Find the image by imd (image ID) and poid (product ID)
    image = db.query(HouseImages).filter_by(poid=poid, imd=imd).first()

    if not image:
        raise HTTPException(status_code=404, detail="Image not found")

    # Delete the image record
    db.delete(image)
    db.commit()

    return {"result": "success", "message": "Image deleted successfully"}



@user.get("/products-with-offers/")
async def get_products_with_offers(db: Session = Depends(get_db)):
    """
    Fetch all products with their offers, if any.
    """
    products = db.query(HouseProducts).filter(
        ~HouseProducts.poid.in_(
            db.query(Subscription.poid).filter(Subscription.status == "active")
        )
    ).all()

    if not products:
        return {"result": "error", "message": "No available products found"}

    result = []
    for product in products:
        price = db.query(Price).filter_by(poid=product.poid).first()
        offer = db.query(HouseOffers).filter_by(poid = product.poid).first()

        result.append({
            "id": product.poid,
            "name": product.name,
            "image": product.image,
            "category": product.category,
            "price": price.amount if price else "N/A",
            "offer": {
                "id": offer.oid,
                "discountPercentage": offer.discountpercentage,
                "startDate": offer.startdate,
                "endDate": offer.enddate,
            } if offer else None,
        })
    return result


@user.post("/product-offer/{product_id}", response_model=OfferResponse)
async def create_offer(product_id: int, offer_data: OfferCreate, db: Session = Depends(get_db)):
    """
    Create a new offer for a product.
    """
    product = db.query(HouseProducts).filter(HouseProducts.poid == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    new_offer = HouseOffers(
        poid=product_id,
        discountpercentage=offer_data.discountPercentage,
        startdate=offer_data.startDate,
        enddate=offer_data.endDate,
        status=0,
    )
    db.add(new_offer)
    db.commit()
    db.refresh(new_offer)

    return {
        "id": new_offer.oid,
        "poid": new_offer.poid,
        "discountPercentage": new_offer.discountpercentage,
        "startDate": new_offer.startdate,
        "endDate": new_offer.enddate,
    }

@user.put("/product-offer/{offer_id}")
async def update_offer(offer_id: int, offer_data: OfferUpdate, db: Session = Depends(get_db)):
    """
    Update an existing offer.
    """
    offer = db.query(HouseOffers).filter_by(oid = offer_data.id).first()
    if not offer:
        raise HTTPException(status_code=404, detail="Offer not found")

    offer.discountpercentage = offer_data.discountPercentage
    offer.startdate = offer_data.startDate
    offer.enddate = offer_data.endDate
    db.commit()
    db.refresh(offer)

    return {
        "id": offer.oid,
        "poid": offer.poid,
        "discountPercentage": offer.discountpercentage,
        "startDate": offer.startdate,
        "endDate": offer.enddate,
    }

@user.delete("/product-offer/{offer_id}")
async def delete_offer(offer_id: int, db: Session = Depends(get_db)):
    """
    Delete an offer.
    """
    offer = db.query(HouseOffers).filter(HouseOffers.oid == offer_id).first()
    if not offer:
        raise HTTPException(status_code=404, detail="Offer not found")
    
    db.delete(offer)
    db.commit()
    return {"result": "success", "message": "Offer deleted successfully"}

@user.get("/house_product_review_list/")
async def get_product_list(db: Session = Depends(get_db)):
    # Query products that are active (status = 0) and not subscribed (poid not in subscriptions)
    products = db.query(HouseProducts).filter(
        ~HouseProducts.poid.in_(
            db.query(Subscription.poid).filter(Subscription.status == "active")
        )
    ).all()

    if not products:
        return {"result": "error", "message": "No available products found"}

    product_list = []
    for product in products:
        # Fetch the price for each product
        price = db.query(Price).filter_by(poid=product.poid).first()
        features = db.query(HouseProductsFeature).filter_by(poid=product.poid).all()
        technicals = db.query(HouseProductsTechnical).filter_by(poid=product.poid).all()
        images = db.query(HouseImages).filter_by(poid=product.poid).all()
        custom_elements = db.query(HouseProductCustomelements).filter_by(poid=product.poid).all()

        product_data = {
            "id": product.poid,
            "name": product.name,
            "images": [i.images for i in images],
            "image": product.image,
            "planscheme_id": product.planscheme_id,
            "category": product.category,
            "description": product.description,
            "datetime": product.datetime,
            "status": product.status,
            "price": price.amount if price else "N/A",  # Handle case when price is not found
            "originalPrice": 22.00,  # Replace with actual price logic if needed
            "rating": 5,  # Replace with actual rating logic if needed
            "sales": 396,  # Replace with actual sales logic if needed
            "features": [f.name for f in features],
            "technical": [t.name for t in technicals],
            "customElements": [
                {"cpid": ce.cpid, "name": ce.name, "description": ce.description}
                for ce in custom_elements
            ],  # Include custom elements
        }

        product_list.append(product_data)

    return {
        "result": "success",
        "data": product_list,
    }

@user.post("/review-product/{product_id}")
async def review_product(product_id: int, review: ReviewRequest, db: Session = Depends(get_db)):
    """
    Approve or reject a product based on the review.
    """
    # Fetch the product from the database
    product = db.query(HouseProducts).filter(HouseProducts.poid == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    # Update the product status based on the review
    if review.status == 1:  # Approved
        product.status = 1
    elif review.status == 2:  # Rejected
        product.status = 2
    else:
        raise HTTPException(status_code=400, detail="Invalid review status")

    # Optional: Save review notes if provided
    if review.notes:
        product.review_notes = review.notes  # Assuming `review_notes` exists in the model

    db.commit()  # Save changes to the database
    return {
        "result": "success",
        "message": f"Product {product_id} has been {'approved' if review.status == 1 else 'rejected'}.",
    }



@user.post("/send-email/")
async def send_email_endpoint(email_request: EmailRequest):
    """
    Send an email with the specified details.
    """
    try:
        # Call the send_email function
        send_email_support(
            email_request.to_email,
            email_request.subject,
            email_request.body
        )
        return {"result": "success", "message": "Email sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send email api: {str(e)}")


@user.get("/subscription-pricing/plans", response_model=list[Plan])
def get_plans(db: Session = Depends(get_db)):
    plans = db.query(PlanModel).all()

    # Convert includedFeatures from a comma-separated string to a list of integers
    for plan in plans:
        if plan.includedFeatures:
            plan.includedFeatures = [
                int(f) for f in plan.includedFeatures.split(",") if f.strip()
            ]
        else:
            plan.includedFeatures = []  # Ensure it's a valid empty list

    return plans

def generate_planschem_id() -> Union[str, int]:
    return random.randint(100000, 999999)  # Or return str(random.randint(...)) if you prefer as string


@user.post("/subscription-pricing/plans")
def create_plans(plans: List[Plan], db: Session = Depends(get_db)):

    # # Validate the incoming plans data
    for plan in plans:
        print(plan)
        if plan.planscheme_id is None:
            raise HTTPException(
                status_code=400,
                detail="Each plan must have a 'planschem_id' provided by the frontend."
            )
    
    # Create PlanModel objects and add them to the database
    db_plans = [PlanModel(**plan.dict(exclude={"pid"})) for plan in plans]  # Allow planschem_id to be included
    db.add_all(db_plans)
    db.commit()
    
    # Return all the inserted plans
    return db.query(PlanModel).all()

@user.put("/subscription-pricing/plans", response_model=List[Plan])
def update_or_remove_plans(plans: List[Plan], db: Session = Depends(get_db)):
    """
    Updates the plans in the database based on the provided payload.
    Removes plans that are not part of the payload.
    Also updates the includedFeatures for each plan.
    """

    # Extract all plan IDs from the request payload
    payload_plan_ids = {plan.pid for plan in plans if plan.pid}

    # Fetch all existing plans for the given planscheme_id
    if not plans:
        raise HTTPException(
            status_code=400,
            detail="Payload must contain at least one plan."
        )
    planscheme_id = plans[0].planscheme_id
    existing_plans = db.query(PlanModel).filter(PlanModel.planscheme_id == planscheme_id).all()

    # Create a mapping of existing plans by their IDs for easier lookup
    existing_plan_ids = {plan.pid for plan in existing_plans}

    # Update or create new plans
    for plan_data in plans:
        if plan_data.pid and plan_data.pid in existing_plan_ids:
            # Update existing plan
            existing_plan = db.query(PlanModel).filter(PlanModel.pid == plan_data.pid).first()
            existing_plan.name = plan_data.name
            existing_plan.base_price = plan_data.base_price
            existing_plan.description = plan_data.description

            # Update included features
            if plan_data.includedFeatures:
                included_features = ",".join(map(str, plan_data.includedFeatures))
                existing_plan.includedFeatures = included_features
            else:
                existing_plan.includedFeatures = None

        else:
            # Add new plan
            included_features = ",".join(map(str, plan_data.includedFeatures)) if plan_data.includedFeatures else None
            new_plan = PlanModel(
                name=plan_data.name,
                base_price=plan_data.base_price,
                description=plan_data.description,
                planscheme_id=plan_data.planscheme_id,
                includedFeatures=included_features,
            )
            db.add(new_plan)

    # Remove plans that are not part of the payload
    plans_to_remove = db.query(PlanModel).filter(
        PlanModel.planscheme_id == planscheme_id,
        PlanModel.pid.not_in(payload_plan_ids)
    ).all()
    for plan in plans_to_remove:
        db.delete(plan)

    # Commit changes to the database
    db.commit()

    # Return the updated list of plans for the given planscheme_id
    updated_plans = db.query(PlanModel).filter(PlanModel.planscheme_id == planscheme_id).all()

    # Convert includedFeatures from a comma-separated string back to a list
    for plan in updated_plans:
        if plan.includedFeatures:
            plan.includedFeatures = [int(f) for f in plan.includedFeatures.split(",")]

    return updated_plans

    
@user.delete("/subscription-pricing/plans/{plan_id}")
def delete_plan(plan_id: int, db: Session = Depends(get_db)):
    plan = db.query(PlanModel).filter(PlanModel.pid == plan_id).first()
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    db.delete(plan)
    db.commit()
    return {"message": "Plan deleted successfully"}



@user.get("/plans/{planscheme_id}", response_model=List[Plan])
def get_plans_by_planscheme_id(planscheme_id: int, db: Session = Depends(get_db)):
    """
    Retrieves plans by the given planscheme_id.
    """
    plans = db.query(PlanModel).filter(PlanModel.planscheme_id == planscheme_id).all()
    
    if not plans:
        raise HTTPException(status_code=404, detail="No plans found for this planscheme_id")
    
    # Deserialize the 'includedFeatures' string into a list of integers
    for plan in plans:
        if plan.includedFeatures:
            plan.includedFeatures = [int(feature) for feature in plan.includedFeatures.split(',')]
    
    return plans

# Routes for features
@user.get("/subscription-pricing/features", response_model=list[Feature])
def get_features(db: Session = Depends(get_db)):
    features = db.query(FeatureModel).all()
    return features

@user.post("/subscription-pricing/features")
def create_features(
    request: FeaturesRequest,  # Corrected to expect FeaturesRequest
    db: Session = Depends(get_db),
):
    # Normalize input to a list of features
    db_features = [
        FeatureModel(name=feature.name, price=feature.price, plan_id=feature.plan_id)
        for feature in request.features
    ]

    # Add and commit features to the database
    db.add_all(db_features)
    db.commit()
    
    # Return the newly added features
    return db.query(FeatureModel).all()


@user.put("/subscription-pricing/features/{feid}", response_model=Feature)
def update_feature(feid: int, feature: Feature, db: Session = Depends(get_db)):
    """
    Updates a feature in the database based on the provided feature ID (feid).
    """
    # Find the existing feature in the database
    db_feature = db.query(FeatureModel).filter(FeatureModel.feid == feid).first()

    if not db_feature:
        raise HTTPException(
            status_code=404,
            detail=f"Feature with ID {feid} not found."
        )

    # Update the feature's details
    db_feature.name = feature.name
    db_feature.price = feature.price
    db_feature.plan_id = feature.plan_id

    # Commit changes to the database
    db.commit()
    db.refresh(db_feature)  # Refresh the instance with the latest data from the database

    # Return the updated feature
    return db_feature
    

@user.delete("/subscription-pricing/features/{feid}")
def delete_feature(feid: int, db: Session = Depends(get_db)):
    feature = db.query(FeatureModel).filter(FeatureModel.feid == feid).first()
    if not feature:
        raise HTTPException(status_code=404, detail="Feature not found")
    db.delete(feature)
    db.commit()
    return {"message": "Feature deleted successfully"}

@user.get("/house_product_list_home/")
async def get_product_list(db: Session = Depends(get_db)):
    # Query products that are active (status = 1) and not subscribed (poid not in subscriptions)
    base_query = db.query(HouseProducts).filter(
        HouseProducts.status == 1,
        ~HouseProducts.poid.in_(
            db.query(Subscription.poid).filter(Subscription.status == "active")
        )
    )
    
    # Fetch the most recently added 5 products
    recent_products = base_query.order_by(HouseProducts.datetime.desc()).limit(5).all()
    
    # Fetch the top-rated 5 products (assuming a `rating` column exists in HouseProducts)
    top_rated_products = base_query.order_by(HouseProducts.datetime.desc()).limit(5).all()

    def get_product_data(product):
        # Fetch related data for the product
        features = db.query(HouseProductsFeature).filter_by(poid=product.poid).all()
        technicals = db.query(HouseProductsTechnical).filter_by(poid=product.poid).all()
        images = db.query(HouseImages).filter_by(poid=product.poid).all()
        offer = db.query(HouseOffers).filter_by(poid=product.poid).first()
        
        # Fetch the first plan associated with the product's planscheme_id
        plan = db.query(PlanModel).filter(PlanModel.planscheme_id == product.planscheme_id).first()
        plan_name = plan.name if plan else "N/A"
        base_price = plan.base_price if plan else "N/A"

        # Calculate the total feature price for the same planscheme_id
        feature_prices = db.query(FeatureModel).filter(
            FeatureModel.plan_id == product.planscheme_id
        ).all()
        total_feature_price = sum(f.price for f in feature_prices) if feature_prices else 0

        # Replace the price with the sum of the base price and total feature price
        combined_price = base_price + total_feature_price if base_price != "N/A" else "N/A"
        if combined_price == "N/A":
            return None

        return {
            "id": product.poid,
            "name": product.name,
            "images": [i.images for i in images],
            "image": product.image,
            "planscheme_id": product.planscheme_id,
            "category": product.category,
            "description": product.description,
            "datetime": product.datetime,
            "status": product.status,
            "price": combined_price,
            "originalPrice": 22.00,  # Replace with actual price logic if needed
            "rating": 5,  # Replace with actual rating logic
            "sales": 396,  # Replace with actual sales logic if needed
            "features": [f.name for f in features],
            "technical": [t.name for t in technicals],
            "offer": {
                "id": offer.oid,
                "discountPercentage": offer.discountpercentage,
                "startDate": offer.startdate,
                "endDate": offer.enddate,
            } if offer else None,
            "plan_name": plan_name,
        }

    recent_product_list = [get_product_data(product) for product in recent_products if get_product_data(product)]
    top_rated_product_list = [get_product_data(product) for product in top_rated_products if get_product_data(product)]

    return {
        "result": "success",
        "recent_products": recent_product_list,
        "top_rated_products": top_rated_product_list,
    }


@user.post("/house_product_device_image_upload/")
async def upload_house_product_device_images(
    poid: int = Form(...),  # Product ID
    files: List[UploadFile] = File(...),  # List of image files
    device_names: List[str] = Form(...),  # Corresponding device names for each file
    db: Session = Depends(get_db),
):
    """
    Upload device-specific images for a product.

    Parameters:
    - poid: Product ID
    - files: List of image files
    - device_names: List of device names corresponding to each image
    """
    if not poid:
        raise HTTPException(status_code=400, detail="Product ID (poid) is required")

    if not files or len(files) == 0:
        raise HTTPException(status_code=400, detail="No files provided for upload")

    if len(files) != len(device_names):
        raise HTTPException(
            status_code=400,
            detail="Number of files and device names must match",
        )

    # Process each file and device name
    uploaded_images = []
    for file, device_name in zip(files, device_names):
        # Validate device name
        if not device_name.strip():
            raise HTTPException(
                status_code=400,
                detail="Device name cannot be empty",
            )

        # Upload image to ImgBB or other service
        image_url = await upload_image_to_imgbb(file)

        # Save image and device details in the database
        device_image = HouseDeviceImages(
            poid=poid,
            device_name=device_name,
            image_url=image_url,
        )
        db.add(device_image)

        uploaded_images.append({"device_name": device_name, "image_url": image_url})

    # Commit all changes to the database
    db.commit()

    return {
        "result": "success",
        "uploaded_images": uploaded_images,
    }

@user.post("/house_product_device_image_delete/")
async def delete_device_image(poid: int, dimd: int, db: Session = Depends(get_db)):
    # Find the image by imd (image ID) and poid (product ID)
    deviceimage = db.query(HouseDeviceImages).filter_by(poid=poid, dimd=dimd).first()

    if not deviceimage:
        raise HTTPException(status_code=404, detail="Image not found")

    # Delete the image record
    db.delete(deviceimage)
    db.commit()

    return {"result": "success", "message": "Image deleted successfully"}



@user.get("/house_product_customize/{product_id}")
async def get_product_details(product_id: int, db: Session = Depends(get_db)):
    product = db.query(HouseProducts).filter_by(poid=product_id).first()
    if not product:
        return {"result": "error", "message": "Product not found"}

    device_images = db.query(HouseDeviceImages).filter_by(poid=product.poid).all()
    custom_elements = db.query(HouseProductCustomelements).filter_by(poid=product.poid).all()

    device_image_data = {}
    for device_image in device_images:
        device_image_data[device_image.device_name] = device_image.image_url

    customizableElements_data = [
        {
            "name": device_image.device_name,
            "description": device_image.image_url,
        }
        for device_image in device_images
    ]

    response = {
        "result": "success",
        "data": {
            "id": product.poid,
            "images": product.image,
            "name": product.name,
            "description": product.description,
            "images": device_image_data,
            "customizableElements": [
                {"name": ce.name, "description": ce.description}
                for ce in custom_elements
            ], 
        }
    }

    return response



@user.post("/submit_customization_requests/{template_id}")
async def submit_customization_requests(template_id: int,payload: CustomizationRequestPayload, db: Session = Depends(get_db)):
    try:
        # Ensure that each customization group (Header, Product Card, etc.) is processed correctly
        for group_name, descriptions in payload.customizationRequests.items():
            if not isinstance(descriptions, list):  # Check if descriptions are in a list format
                raise ValueError(f"Expected list for descriptions, but got {type(descriptions)}.")
            
            for description in descriptions:
                # Create a new customization request entry in the database
                new_request = CustomizationRequest(
                    poid=payload.poid,  # The template ID
                    id=payload.id,  # Customization ID
                    name=group_name,  # The group name (e.g., "Header", "Product Card")
                    customize=description,  # The customization description
                    status=0,  # Default to status 0 (inactive)
                )
                db.add(new_request)  # Add the request to the session

        db.commit()  # Save all requests to the database
        return {"result": "success", "message": "Customization requests submitted successfully"}

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))  # Handle specific ValueError if descriptions aren't a list
    except Exception as e:
        db.rollback()  # Rollback in case of an error
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")


@user.get("/customization_requests_with_details/")
async def get_all_customization_requests_with_details(db: Session = Depends(get_db)):
    try:
        # Fetch all customization requests
        customization_requests = db.query(
            CustomizationRequest.name,
            CustomizationRequest.customize,
            CustomizationRequest.status,
            CustomizationRequest.poid,
            CustomizationRequest.rid,
            CustomizationRequest.id,
        ).all()

        if not customization_requests:
            return {"result": "error", "message": "No customization requests found"}

        # Group customization requests by 'poid' and 'rid'
        grouped_requests_by_poid: Dict[tuple, List[Dict[str, Union[str, Dict[str, int]]]]] = {}
        for name, customize, status, poid, rid, id in customization_requests:
            key = (poid, id)  # Grouping key: poid + rid
            if key not in grouped_requests_by_poid:
                grouped_requests_by_poid[key] = []
            grouped_requests_by_poid[key].append({
                "name": name,
                "customize": customize,
                "status": {"value": status, "rid": rid}  # Include rid in the status object
            })

        # Prepare the response data
        response_data = []

        # Iterate over grouped requests
        for (poid, id), customizations in grouped_requests_by_poid.items():
            # Fetch user details (use rid as user_id)
            user = db.query(Houseuser).filter(Houseuser.id == id).first()
            if not user:
                raise HTTPException(status_code=404, detail="User not found")

            # Fetch product details
            product = db.query(HouseProducts).filter(HouseProducts.poid == poid).first()
            if not product:
                raise HTTPException(status_code=404, detail="Product not found")

            # Group customizations by 'name'
            grouped_customizations_by_name: Dict[str, List[Dict[str, Union[str, Dict[str, int]]]]] = {}
            for customization in customizations:
                name = customization["name"]
                if name not in grouped_customizations_by_name:
                    grouped_customizations_by_name[name] = []
                grouped_customizations_by_name[name].append({
                    "customization": customization["customize"],
                    "status": customization["status"]
                })

            # Create a list of grouped customization objects
            customization_groups = [
                CustomizationGroup(
                    name=name,
                    customizations=[{
                        "customization": item["customization"],
                        "status": item["status"]
                    } for item in customizes]
                )
                for name, customizes in grouped_customizations_by_name.items()
            ]

            # Add the entry to the response
            response_data.append({
                "user_details": {
                    "user_id": user.id,
                    "username": user.username,
                    "email": user.email
                },
                "product_details": {
                    "poid": product.poid,
                    "name": product.name,
                    "description": product.description,
                    "category": product.category,
                    "image": product.image
                },
                "customization_requests": customization_groups
            })

        return response_data

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")


@user.post("/update_customization_status/")
async def update_customization_status(
    request: UpdateCustomizationStatusRequest, db: Session = Depends(get_db)
):
    try:
        # Fetch the customization request by rid
        customization_request = db.query(CustomizationRequest).filter(CustomizationRequest.rid == request.rid).first()
        
        if not customization_request:
            raise HTTPException(status_code=404, detail="Customization request not found")
        
        # Update the status of the customization request
        customization_request.status = request.new_status
        
        # Commit the changes to the database
        db.commit()
        
        return {"result": "success", "message": "Customization request status updated"}
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")



@user.get("/customization_requests_with_details_users/{userid}")
async def get_all_customization_requests_with_details(userid:int, db: Session = Depends(get_db)):
    try:
        # Fetch all customization requests
        customization_requests = db.query(
            CustomizationRequest.name,
            CustomizationRequest.customize,
            CustomizationRequest.status,
            CustomizationRequest.poid,
            CustomizationRequest.rid,
            CustomizationRequest.id,
        ).filter_by(id=userid).all()

        if not customization_requests:
            return {"result": "error", "message": "No customization requests found"}

        # Group customization requests by 'poid' and 'rid'
        grouped_requests_by_poid: Dict[tuple, List[Dict[str, Union[str, Dict[str, int]]]]] = {}
        for name, customize, status, poid, rid, id in customization_requests:
            key = (poid, id)  # Grouping key: poid + rid
            if key not in grouped_requests_by_poid:
                grouped_requests_by_poid[key] = []
            grouped_requests_by_poid[key].append({
                "name": name,
                "customize": customize,
                "status": {"value": status, "rid": rid}  # Include rid in the status object
            })

        # Prepare the response data
        response_data = []

        # Iterate over grouped requests
        for (poid, id), customizations in grouped_requests_by_poid.items():
            # Fetch user details (use rid as user_id)
            user = db.query(Houseuser).filter(Houseuser.id == id).first()
            if not user:
                raise HTTPException(status_code=404, detail="User not found")

            # Fetch product details
            product = db.query(HouseProducts).filter(HouseProducts.poid == poid).first()
            if not product:
                raise HTTPException(status_code=404, detail="Product not found")

            # Group customizations by 'name'
            grouped_customizations_by_name: Dict[str, List[Dict[str, Union[str, Dict[str, int]]]]] = {}
            for customization in customizations:
                name = customization["name"]
                if name not in grouped_customizations_by_name:
                    grouped_customizations_by_name[name] = []
                grouped_customizations_by_name[name].append({
                    "customization": customization["customize"],
                    "status": customization["status"]
                })

            # Create a list of grouped customization objects
            customization_groups = [
                CustomizationGroup(
                    name=name,
                    customizations=[{
                        "customization": item["customization"],
                        "status": item["status"]
                    } for item in customizes]
                )
                for name, customizes in grouped_customizations_by_name.items()
            ]

            # Add the entry to the response
            response_data.append({
                "user_details": {
                    "user_id": user.id,
                    "username": user.username,
                    "email": user.email
                },
                "product_details": {
                    "poid": product.poid,
                    "name": product.name,
                    "description": product.description,
                    "category": product.category,
                    "image": product.image
                },
                "customization_requests": customization_groups
            })

        return response_data

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")

@user.get("/subscription_list")
def get_subscription_list(db: Session = Depends(get_db)):
    try:
        subscriptions = db.query(Subscription).all()
        response_data = []
        
        for subscription in subscriptions:
            # Parse selected features
            selected_features = subscription.selected_features.split(",") if subscription.selected_features else []
            feature_list = []
            
            for feature in selected_features:
                features = db.query(FeatureModel).filter_by(feid=feature).first()
                if features is None:
                    feature_list.append({"name": "Unknown Feature"})
                else:
                    feature_list.append({"name": features.name})

            user = db.query(Houseuser).filter(Houseuser.id == subscription.id).first()
            if not user:
                raise HTTPException(status_code=404, detail="User not found")

            product = db.query(HouseProducts).filter(HouseProducts.poid == subscription.poid).first()
            if not product:
                raise HTTPException(status_code=404, detail="Product not found")

            response_data.append({
                "user_details": {
                    "user_id": user.id,
                    "username": user.username,
                    "email": user.email
                },
                "product_details": {
                    "poid": product.poid,
                    "name": product.name,
                    "description": product.description,
                    "category": product.category,
                    "image": product.image
                },
                "suid":subscription.suid,
                "plan_name":subscription.plan_name,
                "amount":subscription.amount,
                "payment_method":subscription.payment_method,
                "type_payment":subscription.type_payment,
                "billing_cycle":subscription.billing_cycle,
                "status":subscription.status,
                "billing_date":subscription.billing_date,
                "expiration_date":subscription.expiration_date,
                "current_price":subscription.current_price,
                "created_at":subscription.created_at,
                "feature_list": feature_list
            })

        return response_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")
