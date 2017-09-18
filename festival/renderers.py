from django_medusa.renderers import StaticSiteRenderer

from . import models


class ArtFestivalRenderer(StaticSiteRenderer):
    def get_paths(self):
        paths = set()
        paths.add('/artfestival/art/')
        paths.add('/artfestival/artists/')
        artists = models.Artist.objects.all()
        # for artist in artists:
        #     paths.add(artist.get_absolute_url())
        #     paths.add('/artfestival/artists/')
        artists = set()
        for art in models.Art.objects.all(): #filter(project_x__festival__year=2017):
            paths.add('/artfestival/art/{}/{}/'.format(art.project_x.festival.year, art.project_x.project.slug))
            artists.add(art.artist)
        for project in models.ProjectSeason.objects.all(): #filter(festival__year=2017):
            paths.add(paths.add(project.get_absolute_url()))
        for artist in artists:
            paths.add(artist.get_absolute_url())
            paths.add('/artfestival/artists/')
        return list(paths)
    

renderers = [ArtFestivalRenderer, ]