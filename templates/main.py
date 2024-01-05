from fastapi import FastAPI, Depends, HTTPException
from .item import Item

from . import model
from .database import SessionLocal, engine

from sqlalchemy.orm import Session

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

model.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

#tasks = []

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/tasks/")
async def view_items(db: Session = Depends(get_db)):
    return db.query(model.Task).all()

@app.get("/tasks/{id}/")
async def view_item(id: int, db: Session = Depends(get_db)):
    return db.query(model.Task).filter(model.Task.id == id).first()

@app.post("/tasks/")
async def create_item(item: Item, db: Session = Depends(get_db)):
    db_task = model.Task(name=item.name, description = item.description, status=item.status)
    db.add(db_task)
    db.commit()
    return {"message": "Task append successfully"}

@app.put("/tasks/{id}/")
async def update_item(id: int, item: Item, db: Session = Depends(get_db)):
    db_task = db.query(model.Task).filter(model.Task.id == id).first()
    db_task.name = item.name
    db_task.description = item.description
    db_task.status = item.status
    db.commit()
    return {"message": "Task update successfully"}

@app.delete("/tasks/{id}/")
async def delete_item(id: int, db: Session = Depends(get_db)):
    db_item = db.query(model.Task).filter(model.Task.id == id).first()
    db.delete(db_item)
    db.commit()
    return {"message": "Task deleted successfully"}