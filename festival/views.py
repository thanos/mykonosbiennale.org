import random
from django.shortcuts import render


from django.http import Http404
from django.shortcuts import render_to_response
from django.views.generic import ListView,DetailView

import models


from pages.views import PageMixin


class ArtList(PageMixin, ListView):
    queryset = models.Art.objects.filter(pk=1)
    def seo(self, context):
        return {
            'title': 'Mykonos Biennale 2015 - Biennale Art',
            'description': "The complete list of art shown in the Mykonos Biennale",
            'url': "/artfestival/art", 
        }

    def get_context_data(self, **kwargs):
        context = super(ArtList, self).get_context_data(**kwargs)
        #a = [(artist, random.choice([ar for ar in artist.art_set.all()])) for artist in models.Artist.objects.filter(visible=True) if artist.art_set.count()]
        a = [random.choice([ar for ar in artist.art_set.all()]) for artist in models.Artist.objects.filter(visible=True) if artist.art_set.count()]
        random.shuffle(a)
        context['art_shown'] = a
        context['choice'] = models.Project.objects.get(slug='treasure-hunt')
        context['projects'] = (project for project in models.Project.objects.all() if project.art_set.count())
        
        return context

class ArtistList(PageMixin, ListView):
    queryset = models.Artist.objects.filter(visible=True).order_by('name')
    def seo(self, context):
        return {
            'title': 'Mykonos Biennale 2015 - Antidote Artists',
            'description': "The complete list of artists partisipating in the Mykonos Biennale",
            'url': "/artfestival/artists", 
        }

class TreasureHuntArtists(PageMixin, ListView):
    queryset = models.Artist.objects.filter(visible=True, event=models.Artist.TEASURE_HUNT).order_by('name')
    def seo(self, context):
        return {
            'title': 'Mykonos Biennale 2015 - Antidote Treasure Hunt Artists',
            'description': "The list of artists partisipating in the Mykonos Biennale Treasure Hunt",
            'url': "/artfestival/artists", 
        }
        
class ArtistDetail(PageMixin, DetailView):
    model = models.Artist

    def breadcrumbs(self, context):
        artist = context['object']
        return [('/', artist.festival), ('/artfestival/artists/', artist.event), ('', artist.name )]

    def seo(self, context):
        artist = self.getObject(context)
        title =  "Mykonos Biennale 2015 - {} - {}".format(artist.event, artist.name)
        description = "Biennale page for {}".format(artist.name)
        url = "/artfestival/artist/{}".format(artist.slug)
        image = artist.artwork() 
        if not image: image = artist.headshot.url if artist.headshot else ''
        return {
            'title': title,
            'description': description,
            'url': url,
             'image': image,    
        }
