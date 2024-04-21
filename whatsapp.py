from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import ai as AI
import whatsapp_helper as whatsappHelper
from database_utils import engine, SessionLocal
from database_models import create_all_tables, User

app = Flask(__name__)

create_all_tables(engine)

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    incoming_number = whatsappHelper.filter_user_number(request.values.get('From', ''))
    print(type(incoming_msg))
    print(incoming_msg)
    print(type(incoming_number))

    ai_response = AI.answer_question(incoming_msg, incoming_number)
    whatsapp_response = whatsappHelper.add_linebreak_and_quote(ai_response)
    msg.body(whatsapp_response)

    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)
