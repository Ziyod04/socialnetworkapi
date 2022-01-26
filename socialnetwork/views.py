from rest_framework import generics
from .models import Post, Like, Dislike
from .serializers import PostSerializer, UserSerializer, LikeSerializer, DislikeSerializer
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from django.http import JsonResponse


class PostList(generics.ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserList(generics.ListCreateAPIView):

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class PostLikeView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class PostDislikeView(generics.CreateAPIView):
    queryset = Dislike.objects.all()
    serializer_class = DislikeSerializer


class PostAnaliticsLikesView(generics.ListAPIView):
    serializer_class = LikeSerializer

    def get(self, request, *args, **kwargs):
        likes_analitic = Like.objects.filter(
            like_published__range=[kwargs['date_from'], kwargs['date_to']])
        if len(likes_analitic) > 0:
            return JsonResponse({'Likes by period': len(likes_analitic)})
        else:
            return self.list(request, *args, [{}])
