from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_models import Data, User
from message_helper import MessageHelper

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def getMessageHistory(phone_no):
    db = SessionLocal()
    message_history = db.query(Data.type, Data.convo).join(User).filter(User.usr_phn == phone_no).all()
    db.close()

    if not message_history:
        return []
    
    transformed_history = []
    for result in message_history:
        transformed_history.append(MessageHelper.transformConversation(result))
    return transformed_history

def userExists(phone_no):
    db = SessionLocal()
    result = db.query(User.usr_id).filter(User.usr_phn == phone_no).first
    if not result:
        return False
    else:
        return True
    
def getUserId(phone_no):
    db = SessionLocal()
    result = db.query(User.usr_id).filter(User.usr_phn == phone_no).first()
    return result[0]

def update_db_conversation(user_id, type, convo):
    db = SessionLocal()
    try:
        new_data = Data(user_id=user_id, type=type, convo=convo)
        db.add(new_data)
        db.commit()
    except Exception as e:
        db.rollback()
        raise e

    finally:
        db.close()

def add_new_user(phone_no):
    db = SessionLocal()
    db_item = User(usr_phn = phone_no)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    db.close()
    return db_item.usr_id
