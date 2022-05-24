from django.contrib import admin
from django.urls import path, include
from .views import AlbumList, SongList

urlpatterns = [
    path('albums/', AlbumList.as_view()),
    path('songs/', SongList.as_view()),
]