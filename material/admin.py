from django.contrib import admin

from photologue.admin import GalleryAdmin as GalleryAdminDefault
from photologue.models import Gallery
from .models import Album


class AlbumInline(admin.StackedInline):
    model = Album
    can_delete = False
admin.site.register(Album)

class GalleryAdmin(GalleryAdminDefault):
    inlines = [AlbumInline, ]

admin.site.unregister(Gallery)
admin.site.register(Gallery, GalleryAdmin)