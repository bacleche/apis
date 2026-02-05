from django.db import models
from apps.users.models import User
from apps.core.models import BaseModel

class Recommendation(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recommendations")
    title = models.CharField(max_length=255)
    content_type = models.CharField(max_length=50)  # ex: 'manga', 'webtoon', 'fanart'
    score = models.FloatField(default=0)  # pertinence recommandation

    def __str__(self):
        return f"{self.title} for {self.user.username}"

class UserPreference(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="preferences")
    preferences = models.JSONField(default=dict)  # ex: genres, tags, authors

    def __str__(self):
        return f"Preferences of {self.user.username}"

class MoodProfile(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mood_profiles")
    mood = models.CharField(max_length=50)  # ex: 'happy', 'sad', 'excited'
    intensity = models.PositiveIntegerField(default=1)  # échelle 1-10

    def __str__(self):
        return f"MoodProfile of {self.user.username} - {self.mood}"
