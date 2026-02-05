from rest_framework import viewsets, permissions
from .models import Conversation, Message, GroupChat, SyncReading
from .serializers import ConversationSerializer, MessageSerializer, GroupChatSerializer, SyncReadingSerializer
from .permissions import IsParticipantOrAdmin

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated, IsParticipantOrAdmin]

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated, IsParticipantOrAdmin]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

class GroupChatViewSet(viewsets.ModelViewSet):
    queryset = GroupChat.objects.all()
    serializer_class = GroupChatSerializer
    permission_classes = [permissions.IsAuthenticated]

class SyncReadingViewSet(viewsets.ModelViewSet):
    queryset = SyncReading.objects.all()
    serializer_class = SyncReadingSerializer
    permission_classes = [permissions.IsAuthenticated]
