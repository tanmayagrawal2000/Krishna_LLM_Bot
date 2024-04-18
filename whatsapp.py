from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import ai as AI
import whatsapp_helper as whatsappHelper

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    incoming_number = whatsappHelper.filter_user_number(request.values.get('From', ''))

    ai_response = AI.answer_question(incoming_msg, incoming_number)
    
    msg.body(ai_response)

    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)
