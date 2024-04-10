from rest_framework import serializers
from .models import MessageLog

class MessageLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageLog
        fields = ['id', 'content', 'timestamp']
