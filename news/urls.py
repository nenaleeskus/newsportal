from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView
from .views import BaseRegisterView
from .views import upgrade_me

urlpatterns = [
    path('news/', PostList.as_view(), name='news_list'),
    path('articles/', PostList.as_view(), name='articles_list'),
    path('news/search/', PostSearch.as_view(), name='news_search'),
    path('news/<int:pk>', PostDetail.as_view()),
    path('articles/<int:pk>', PostDetail.as_view()),
    path('news/create/', PostCreate.as_view()),
    path('articles/create/', PostCreate.as_view()),
    path('news/<int:pk>/edit/', PostUpdate.as_view()),
    path('articles/<int:pk>/edit/', PostUpdate.as_view()),
    path('news/<int:pk>/delete/', PostDelete.as_view()),
    path('articles/<int:pk>/delete/', PostDelete.as_view()),
    path('upgrade/', upgrade_me, name='upgrade'),
    path('', IndexView.as_view()),
]
