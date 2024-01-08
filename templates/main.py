from typing import List
from fastapi import FastAPI, Depends, HTTPException
from .item import Users, UsersOut, Products, ProductsOut, Orders, OrdersOut

from . import model
from .database import SessionLocal, engine

from sqlalchemy.orm import Session

import logging

from werkzeug.security import generate_password_hash, check_password_hash

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



default_skip = 0
default_limit = 10

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users/", response_model=List[UsersOut])
async def get_users(skip: int = default_skip, limit: int = default_limit, db: Session = Depends(get_db)):
    users = db.query(model.User).offset(skip).limit(limit).all()
    return users

@app.get("/users/{id}/", response_model=UsersOut)
async def get_user(id:int, db: Session = Depends(get_db)):
    return db.query(model.User).filter(model.User.id == id).first()

@app.post("/user/")
async def set_user(obj: Users, db: Session = Depends(get_db)):
    db_user = model.User(surname = obj.surname, name = obj.name, patronymic = obj.patronymic, email = obj.email, password = generate_password_hash(obj.password))
    db.add(db_user)
    db.commit()
    return {'message': 'User append successfully'}

@app.put("/user/{id}/")
async def update_user(id: int, obj: Users, db: Session = Depends(get_db)):
    db_user = db.query(model.User).filter(model.User.id == id).first()
    db_user.surname = obj.surname
    db_user.name = obj.name
    db_user.patronymic = obj.patronymic
    db_user.email = obj.email
    db_user.password = generate_password_hash(obj.password)
    db.commit()
    return {"message": "User update successfully"}

@app.delete("/user/{id}")
async def del_user(id: int, db: Session = Depends(get_db)):
    db_user = db.query(model.User).filter(model.User.id == id).first()
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}

@app.get("/producs/", response_model=List[ProductsOut])
async def get_products(skip: int = default_skip, limit: int = default_limit, db: Session = Depends(get_db)):
    return db.query(model.Products).offset(skip).limit(limit).all()

@app.get("/produc/{id}/", response_model=ProductsOut)
async def get_product(id:int, db: Session = Depends(get_db)):
    return db.query(model.Products).filter(model.User.id == id).first()

@app.post("/produc/")
async def set_product(obj: Products, db: Session = Depends(get_db)):
    db_product = model.Products(name = obj.name, description = obj.description, price = obj.price)
    db.add(db_product)
    db.commit()
    return {'message': 'Product append successfully'}

@app.put("/produc/{id}/")
async def update_product(obj: Products, id:int, db: Session = Depends(get_db)):
    db_product = db.query(model.Products).filter(model.Products.id == id).first()
    db_product.name = obj.name
    db_product.description = obj.description
    db_product.price = obj.price
    db.commit()
    return {"message": "Product update successfully"}

@app.delete("/produc/{id}")
async def del_product(id:int, db: Session = Depends(get_db)):
    db_product = db.query(model.Products).filter(model.Products.id == id).first()
    db.delete(db_product)
    db.commit()
    return {"message": "Product deleted successfully"}

@app.get("/orders/", response_model=List[OrdersOut])
async def get_orders(skip: int = default_skip, limit: int = default_limit, db: Session = Depends(get_db)):
    return db.query(model.Orders).offset(skip).limit(limit).all()

@app.get("/order/{id}/", response_model=OrdersOut)
async def get_order(id:int, db: Session = Depends(get_db)):
    return db.query(model.Orders).filter(model.User.id == id).first()

@app.post("/order/")
async def set_order(obj: Orders, db: Session = Depends(get_db)):
    db_order = model.Orders(id_user = obj.id_user, id_products = obj.id_products, status = obj.status)
    db.add(db_order)
    db.commit()
    return {'message': 'Order append successfully'}

@app.put("/order/{id}/")
async def update_order(obj: Orders, id:int, db: Session = Depends(get_db)):
    db_order = db.query(model.Orders).filter(model.Orders.id == id).first()
    db_order.id_user = obj.id_user
    db_order.id_products = obj.id_products
    db_order.status = obj.status
    db.commit()
    return {"message": "Order update successfully"}

@app.delete("/order/{id}")
async def del_order(id:int, db: Session = Depends(get_db)):
    db_order = db.query(model.Orders).filter(model.Orders.id == id).first()
    db.delete(db_order)
    db.commit()
    return {"message": "Order deleted successfully"}