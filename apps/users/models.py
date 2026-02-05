from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.core.models import BaseModel


class User(AbstractUser):
    email = models.EmailField(unique=True)
    xp = models.PositiveIntegerField(default=0)
    level = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.username


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    bio = models.TextField(blank=True)
    preferences = models.JSONField(default=dict)

    def __str__(self):
        return f"Profile of {self.user.username}"


class Badge(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.ImageField(upload_to="badges/", null=True, blank=True)

    def __str__(self):
        return self.name


class Level(BaseModel):
    level_number = models.PositiveIntegerField()
    required_xp = models.PositiveIntegerField()

    def __str__(self):
        return f"Level {self.level_number}"


class Achievement(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="achievements")
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    date_earned = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} earned {self.badge.name}"
