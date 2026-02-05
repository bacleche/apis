from django.db import models

from apps.users.models import User

from apps.core.models import BaseModel

class Manga(BaseModel):
    STATUS = [("ongoing", "Ongoing"), ("completed", "Completed")]

    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    cover = models.ImageField(upload_to="manga/covers/")
    status = models.CharField(max_length=20, choices=STATUS)
    rating = models.FloatField(default=0)


class Chapter(BaseModel):
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, related_name="chapters")
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField()


class Page(BaseModel):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name="pages")
    image = models.ImageField(upload_to="manga/pages/")
    order = models.PositiveIntegerField()
