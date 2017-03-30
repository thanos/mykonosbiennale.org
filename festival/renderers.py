from django_medusa.renderers import StaticSiteRenderer
from . import models


class ArtFestivalRenderer(StaticSiteRenderer):
    def get_paths(self):
        paths = set()
        paths.add('/artfestival/art/')
        paths.add('/artfestival/artists/')
        artists = models.Artist.objects.all()
        for artist in artists:
            paths.add(artist.get_absolute_url())
        return list(paths)

renderers = [ArtFestivalRenderer, ]