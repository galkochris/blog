from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length=200)
    post = models.CharField(max_length=1600)
    image = models.ImageField(upload_to='posts', default='blog_images')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post,
                                on_delete=models.CASCADE,
                                related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('created',)
    
    def __str__(self):
        return 'Comment by {} on {}'.format(self.author, self.post)

