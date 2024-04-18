from fastapi import FastAPI, HTTPException
from fastapi import Request
from twilio.twiml.messaging_response import MessagingResponse
from database_utils import engine, SessionLocal
from database_models import create_all_tables, User
import ai as AI

create_all_tables(engine)

app = FastAPI()

@app.post("/whatsapp/webhook/")
async def whatsapp_webhook(request: Request):
    form_data = await request.form()
    message_body = form_data.get('Body', '').lower()
    print(message_body)
    resp = MessagingResponse()
    if message_body == 'hello':
        db = SessionLocal()
        count = db.query(User).count()
        db.close()
        print("Hi")
        resp.message("There are currently 5 items in the database")
    else:
        resp.message('Send "hello" to get the count of items in the database.')
    print(str(resp))
    return str(resp)



# r = AI.answer_question("Kya aap hi Ram hai?", 6030)
# print(r)

