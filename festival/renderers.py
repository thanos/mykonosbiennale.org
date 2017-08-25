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
            paths.add('/artfestival/artists/')
        for art in models.Art.objects.all():
            paths.add('/artfestival/art/{}/{}/'.format(art.project_x.festival.year, art.project_x.project.slug))
        for project in models.ProjectSeason.objects.all():
            paths.add(paths.add(project.get_absolute_url()))
        return list(paths)
    

#renderers = [ArtFestivalRenderer, ]