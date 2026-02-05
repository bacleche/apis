from rest_framework import serializers
from .models import Conversation, Message, GroupChat, SyncReading

class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ['sender']

class GroupChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupChat
        fields = '__all__'

class SyncReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SyncReading
        fields = '__all__'
