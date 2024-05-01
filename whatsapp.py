import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import ai as AI
import whatsapp_helper as whatsappHelper
from database_utils import engine, SessionLocal
from database_models import create_all_tables, User
from twilio.rest import Client


app = Flask(__name__)

create_all_tables(engine)

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '')
    resp = MessagingResponse()
    msg = resp.message()
    incoming_number = whatsappHelper.filter_user_number(request.values.get('From', ''))
    
    print(incoming_msg)

    ai_response = AI.answer_question(incoming_msg, incoming_number)
    whatsapp_response = whatsappHelper.add_linebreak_and_quote(ai_response)
    
    account_sid = os.getenv("SID")
    auth_token = os.getenv("AUTH_TOKEN")
    client = Client(account_sid, auth_token)
    print(account_sid)

    message = client.messages.create(
                    from_='whatsapp:+14155238886',
                    body=whatsapp_response,
                    to=f'whatsapp:{incoming_number}'
                    )


    print(message.sid)
    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)