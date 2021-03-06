from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    liked_post = models.ManyToManyField("Post", related_name="likers")

class Post(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="posts")
    content = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    number_of_likes = models.IntegerField(blank=True, null=True)
    
    def serialize(self):
        return {
            "user" : self.id,
            "content" : self.content,
            "timestamp" : self.timestamp.strftime("%b %d %Y, %I:%M %p")
        }