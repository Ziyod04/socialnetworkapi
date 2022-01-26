from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(
        User, related_name='like_user', on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='like_post', on_delete=models.CASCADE)
    like = models.SmallIntegerField(default=0)
    like_published = models.DateField(format('%Y-%m-%d'), auto_now_add=True)


class Dislike(models.Model):
    user = models.ForeignKey(
        User, related_name='dislike_user', on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='dislike_post', on_delete=models.CASCADE)
    dislike = models.SmallIntegerField(default=0)
    dislike_published = models.DateField(format('%Y-%m-%d'), auto_now_add=True)
