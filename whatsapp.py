from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    if 'hello' in incoming_msg:
        msg.body('Hi there! How can I help you today?')
        responded = True

    if not responded:
        msg.body("I'm not sure how to respond to that. Can you try asking something else?")

    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)
