from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from twilio.twiml.messaging_response import MessagingResponse

from .models import MessageLog
from .serializers import MessageLogSerializer

# Twilio WhatsApp Webhook
@csrf_exempt
def whatsapp_webhook(request):
    if request.method == "POST":
        incoming_msg = request.POST.get('Body', '').strip().lower()
        resp = MessagingResponse()
        msg = resp.message()

        # Custom logic to respond with the number of MessageLog entries
        # when the user sends "hi hello"
        if incoming_msg == "hi hello":
            items_count = MessageLog.objects.count()  # Count items in MessageLog
            response_message = f"Hi there! You have {items_count} items in the log."
        else:
            response_message = "Welcome to our WhatsApp service! Send 'hi hello' to get the number of items in the log."

        msg.body(response_message)

        # Optionally, log the incoming message to the database
        MessageLog.objects.create(content=incoming_msg)

        return HttpResponse(str(resp), content_type='text/xml')
    else:
        # Return a method not allowed response if not POST
        return HttpResponse('Method Not Allowed', status=405)

# REST API Viewset
class MessageLogViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing MessageLog entries.
    """
    queryset = MessageLog.objects.all()
    serializer_class = MessageLogSerializer
