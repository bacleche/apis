from django.db import models
from apps.users.models import User
from apps.core.models import BaseModel

class Forum(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

class Thread(BaseModel):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name="threads")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

class Post(BaseModel):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name="posts")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

class Comment(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

class Like(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")

class Club(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    members = models.ManyToManyField(User, related_name="clubs")

class Event(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date = models.DateTimeField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name="events")

class Poll(BaseModel):
    question = models.CharField(max_length=255)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name="polls")
