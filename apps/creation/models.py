from django.db import models
from apps.users.models import User
from apps.core.models import BaseModel

class UserManga(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_mangas")
    title = models.CharField(max_length=255)
    description = models.TextField()
    cover = models.ImageField(upload_to="creation/manga/covers/")

class UserWebtoon(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_webtoons")
    title = models.CharField(max_length=255)
    description = models.TextField()
    cover = models.ImageField(upload_to="creation/webtoons/covers/")

class Fanfiction(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="fanfictions")
    title = models.CharField(max_length=255)
    content = models.TextField()

class Fanart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="fanarts")
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="creation/fanarts/")
