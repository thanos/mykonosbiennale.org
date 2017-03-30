from django_medusa.renderers import StaticSiteRenderer
from . import models


class PagesRenderer(StaticSiteRenderer):
    def get_paths(self):
        paths = ['']
        pages = models.Page.objects.filter(visible=True)
        for page in pages:
            paths.append(page.get_absolute_url())
        print paths
        return paths

      
class Biennale2013Renderer(StaticSiteRenderer):
    def get_paths(self):
        return [
         # '/Mykonos_Biennale_2015/2013_The_Mystic_Party.html'
          
          
        ]      
      
renderers = [PagesRenderer, ]