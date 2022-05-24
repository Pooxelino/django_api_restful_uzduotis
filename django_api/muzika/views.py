from django.shortcuts import render
from rest_framework import generics
from .models import Artist, Album, Song, AlbumReview, AlbumReviewComment, AlbumReviewLike
from .serializers import AlbumSerializer, SongSerializer

# Create your views here.
class AlbumList(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class SongList(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer