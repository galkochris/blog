from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length=200)
    post = models.CharField(max_length=1600)
    image = models.ImageField(upload_to='posts', default='blog_images')
    Author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    title = models.CharField(max_length=50)
    comment = models.CharField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False)
    Author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)