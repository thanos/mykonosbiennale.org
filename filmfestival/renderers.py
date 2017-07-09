from django_medusa.renderers import StaticSiteRenderer

from . import models


#from festival import models as festival_models

class FilmFestivalRenderer(StaticSiteRenderer):
    def get_paths(self):
        paths = set('')
        paths.add('/filmfestival/film/175-rome-churches-patrick-kelley/')
        paths.add('/filmfestival/films/')
        paths.add('/filmfestival/film/')
        paths.add('/filmfestival/dramatic-nights/')
        paths.add('/filmfestival/video-graffiti/')
        films = models.Film.objects.filter(status='SELECTED').order_by('title')
        for film in films:
            paths.add(film.get_absolute_url())
            if film.project ==None:
                print film, "has no project", film.pk
            else:
                paths.add('/filmfestival/{}/{}/'.format(film.project.festival.year, film.project.slug))
        return list(paths)

renderers = [FilmFestivalRenderer, ]