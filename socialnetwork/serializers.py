from rest_framework import serializers
from .models import Post, Like, Dislike
from django.contrib.auth import get_user_model

class PostSerializer(serializers.ModelSerializer):
    class Meta:

        fields = ('id', 'author', 'title', 'body', 'created_at',)
        model = Post

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'last_login')



class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = (
            'user', 'post', 'like', 'like_published'
        )


class DislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislike
        fields = (
            'user', 'post', 'dislike', 'dislike_published'
        )