from django.contrib import admin
from .models import Artist, Album, Song, AlbumReview, AlbumReviewComment, AlbumReviewLike

# Register your models here.

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(AlbumReview)
admin.site.register(AlbumReviewComment)
admin.site.register(AlbumReviewLike)
