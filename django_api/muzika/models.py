from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Artist(models.Model):
    name = models.CharField(verbose_name="Artist name", max_length=150)

    def __str__(self):
        return f"{self.name}"


class Album(models.Model):
    name = models.CharField(verbose_name="Album name", max_length=150)
    artist_id = models.ForeignKey(Artist, verbose_name="Artist ID",  on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Song(models.Model):
    name = models.CharField(verbose_name="Song name", max_length=150)
    duration = models.CharField(verbose_name="Song duration", max_length=150)
    album_id = models.ForeignKey(Album, verbose_name="Album ID", on_delete=models.CASCADE, null=True, blank=True)
    artist_id = models.ForeignKey(Artist, verbose_name="Artist ID", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.duration}"

class AlbumReview(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    album_id = models.ForeignKey(Album, verbose_name="Album ID",  on_delete=models.CASCADE, null=True)
    content = models.TextField(verbose_name="Review content", max_length=1000)
    score = models.CharField(verbose_name="Album score", max_length=150)

    def __str__(self):
        return f"{self.content} {self.score}"

class AlbumReviewComment(models.Model):
    user = models.ForeignKey(User, verbose_name="User",  on_delete=models.CASCADE)
    album_review_id = models.ForeignKey(AlbumReview, verbose_name="Album review ID",  on_delete=models.CASCADE)
    content = models.CharField(verbose_name="Album review comment content", max_length=150)

    def __str__(self):
        return f"{self.user} {self.content}"

class AlbumReviewLike(models.Model):
    user = models.ForeignKey(User, verbose_name="User",  on_delete=models.CASCADE)
    album_review_id = models.ForeignKey(AlbumReview, verbose_name="Album review ID",  on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"