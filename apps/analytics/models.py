from django.db import models
from apps.users.models import User
from apps.core.models import BaseModel

class UserActivity(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="activities")
    action = models.CharField(max_length=255)
    metadata = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.user.username} - {self.action}"

class ReadingStats(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reading_stats")
    manga_read = models.PositiveIntegerField(default=0)
    webtoons_read = models.PositiveIntegerField(default=0)
    pages_read = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"ReadingStats for {self.user.username}"

class Engagement(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="engagements")
    posts_liked = models.PositiveIntegerField(default=0)
    comments_made = models.PositiveIntegerField(default=0)
    time_spent_minutes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Engagement for {self.user.username}"
