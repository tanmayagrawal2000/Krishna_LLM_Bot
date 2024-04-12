from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi import Request
from twilio.twiml.messaging_response import MessagingResponse


DATABASE_URL = "sqlite:///./test.db"
Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class ItemCreate(BaseModel):
    name: str

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/items/")
def create_item(item: ItemCreate):
    db = SessionLocal()
    db_item = Item(name=item.name)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    db.close()
    return db_item

@app.get("/items/count")
def read_items_count():
    db = SessionLocal()
    count = db.query(Item).count()
    db.close()
    return {"count": count}

@app.post("/whatsapp/webhook/")
async def whatsapp_webhook(request: Request):
    form_data = await request.form()
    message_body = form_data.get('Body', '').lower()
    resp = MessagingResponse()
    if message_body == 'hello':
        db = SessionLocal()
        count = db.query(Item).count()
        db.close()
        resp.message(f'There are currently {count} items in the database.')
    else:
        resp.message('Send "hello" to get the count of items in the database.')
    return str(resp)
