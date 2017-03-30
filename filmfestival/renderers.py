from django_medusa.renderers import StaticSiteRenderer
from . import models


class FilmFestivalRenderer(StaticSiteRenderer):
    def get_paths(self):
        paths = set()
        paths.add('/filmfestival/films/')
        paths.add('/filmfestival/video-graffiti/')
        paths.add('/filmfestival/dramatic-nights/')
        films = models.Film.objects.filter(status='SELECTED').order_by('title')
        for film in films:
            paths.add(film.get_absolute_url())
        return list(paths)

renderers = [FilmFestivalRenderer, ]