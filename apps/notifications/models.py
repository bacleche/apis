from django.db import models
from apps.users.models import User
from apps.core.models import BaseModel


class Notification(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message}"


class NotificationPreference(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="notification_preferences")
    email_notifications = models.BooleanField(default=True)
    push_notifications = models.BooleanField(default=True)

    def __str__(self):
        return f"Notification Preferences for {self.user.username}"
