from rest_framework import serializers
from .models import Artist, Album, Song, AlbumReview, AlbumReviewComment, AlbumReviewLike

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'name', 'artist_id']

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'name', 'duration', 'artist_id', 'album_id']