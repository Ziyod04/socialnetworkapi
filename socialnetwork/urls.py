from django.urls import path
from .views import PostList, PostDetail, UserList, UserDetail, PostAnaliticsLikesView, PostLikeView, PostDislikeView


urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),

    path('post/<int:pk>/', PostDetail.as_view()),
    path('post/', PostList.as_view()),
    path('post/<int:pk>/like/',PostLikeView.as_view()),
    path('post/<int:pk>/dislike/',PostDislikeView.as_view()),

    
    path('analitics/date_from=<date_from>&date_to=<date_to>/', PostAnaliticsLikesView.as_view()),

]
