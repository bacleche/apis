from django.db import models
from apps.users.models import User
from apps.core.models import BaseModel

class Conversation(BaseModel):
    participants = models.ManyToManyField(User, related_name="conversations")

    def __str__(self):
        return f"Conversation {self.id}"

class Message(BaseModel):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f"Message {self.id} by {self.sender.username}"

class GroupChat(BaseModel):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name="group_chats")

    def __str__(self):
        return self.name

class SyncReading(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    page_number = models.PositiveIntegerField(default=1)
