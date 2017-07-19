import collections
import random

from bakery.views import BuildableListView, BuildableDetailView
from django.http import Http404
from django.views.generic import DetailView, ListView

import models
from pages.views import PageMixin


class ProjectDetail(PageMixin, DetailView):
    queryset = models.ProjectX.objects.all()
    template_name='festival/project_detail.html'
      
    def seo(self, context):
        return {
            'title': 'Mykonos Biennale 2015 - Biennale Art',
            'description': "The complete list of art shown in the Mykonos Biennale",
            'url': "/artfestival/art", 
        }

#     def get(self, request, *args, **kwargs):
#         if kwargs['slug'] =='all':
#            kwargs['slug'] = 'treause-hunt' #{'slug':'all'}
#         #else:
#         self.object = self.get_object()
#         context = self.get_context_data(object=self.object)
#         return self.render_to_response(context)   
    
    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug', 'all')
        year= self.kwargs.get('year', '2017')
        
        if not queryset:
            queryset = self.queryset
        queryset = queryset.filter(festival__year=int(year))
        try:
            return super(ProjectDetail, self).get_object(queryset)
        except Http404:
            if slug != 'all':
                raise
            return dict(slug='')
    
    def get_context_data(self, **kwargs):
        context = super(ProjectDetail, self).get_context_data(**kwargs)
        #a = [(artist, random.choice([ar for ar in artist.art_set.all()])) for artist in models.Artist.objects.filter(visible=True) if artist.art_set.count()]
        #a = [random.choice([ar for ar in artist.art_set.all()]) for artist in models.Artist.objects.filter(visible=True) if artist.art_set.count()]
        year = self.kwargs.get('year', '2017')
        context['year'] = year
        context['art_shown'] = (art for art in models.Art.objects.filter(leader=True, project_x__festival__year=year) if art.artist.visible)
        #random.shuffle(context['art_shown'])
        context['projects']= (ps.project for ps in models.ProjectSeason.objects.all() if ps.art_set.count())
        #context['years'] = set(project.year for project in context['projects'] )
        return context



class ArtList(PageMixin, BuildableListView):
    queryset = models.Art.objects.filter(pk=1)
    def seo(self, context):
        return {
            'title': 'Mykonos Biennale 2015 - Biennale Art',
            'description': "The complete list of art shown in the Mykonos Biennale",
            'url': "/artfestival/art", 
        }

    def get_context_data(self, **kwargs):
        print kwargs
        context = super(ArtList, self).get_context_data(**kwargs)
        #a = [(artist, random.choice([ar for ar in artist.art_set.all()])) for artist in models.Artist.objects.filter(visible=True) if artist.art_set.count()]
        #a = [random.choice([ar for ar in artist.art_set.all()]) for artist in models.Artist.objects.filter(visible=True) if artist.art_set.count()]
        a = [art for art in models.Art.objects.filter(leader=True) if art.artist.visible]
        random.shuffle(a)
        context['art_shown'] = a
        project_slug = self.request.GET.get('project')
        context['choice'] = models.ProjectX.objects.get(slug=project_slug) if project_slug else 'all'
        context['projects'] = (project for project in models.ProjectX.objects.all() if project.art_set.count())
        
        return context

class ArtistList(PageMixin, ListView):
    queryset = models.Artist.objects.filter(visible=True).order_by('name')
    def seo(self, context):
        return {
            'title': 'Mykonos Biennale 2015 - Antidote Artists',
            'description': "The complete list of artists partisipating in the Mykonos Biennale",
            'url': "/artfestival/artists", 
        }

    def get_context_data(self, **kwargs):
        context = super(ArtistList, self).get_context_data(**kwargs)
        #a = [(artist, random.choice([ar for ar in artist.art_set.all()])) for artist in models.Artist.objects.filter(visible=True) if artist.art_set.count()]
        #a = [random.choice([ar for ar in artist.art_set.all()]) for artist in models.Artist.objects.filter(visible=True) if artist.art_set.count()]
        year = self.kwargs.get('year', '2017')
        context['year'] = year
        context['artists'] = set(art.artist for art in models.Art.objects.filter(leader=True, project_x__festival__year=year) if art.artist.visible)
        random.shuffle(list(context['artists']))
        return context

    def get_context_data(self, **kwargs):
        context = super(ArtistList, self).get_context_data(**kwargs)
        #a = [(artist, random.choice([ar for ar in artist.art_set.all()])) for artist in models.Artist.objects.filter(visible=True) if artist.art_set.count()]
        #a = [random.choice([ar for ar in artist.art_set.all()]) for artist in models.Artist.objects.filter(visible=True) if artist.art_set.count()]
        context['year'] = self.kwargs.get('year')
        artists = collections.default(set)
        festivals = set()
        projects = set()
        for art in models.Art.objects.filter(leader=True):
            artists[art.artist].add(art.project_x)
            artists[art.artist].add(art.project_x.festival)
            festivals.add(art.project_x.festival)
            projects.add(art.project_x.project)
        #if context['year']:
        #    art_q = art_q.filter(leader=True, project_x__festival__year=context['year'])
        art = [art for art in art_q]
        artists = list(set(art.artist for art in art))
        random.shuffle(artists)
        context['artists'] = artists

        context['festivals'] = festivals
        context['projects'] = projects
        return context

    def get_context_data(self, **kwargs):
        context = super(ArtistList, self).get_context_data(**kwargs)
        #a = [(artist, random.choice([ar for ar in artist.art_set.all()])) for artist in models.Artist.objects.filter(visible=True) if artist.art_set.count()]
        #a = [random.choice([ar for ar in artist.art_set.all()]) for artist in models.Artist.objects.filter(visible=True) if artist.art_set.count()]
        project = self.kwargs.get('project')
        year = self.kwargs.get('year', '2017' if project else None)
        art_q  =  models.Art.objects.all()
        if year:
            context['festival'] = models.Festival.objects.filter(year=year)[0]
            art_q = models.Art.objects.filter(project_x__festival= context['festival'])
            if project:
                context['project'] = models.SeasonProject.objects.filter(project_name=project, festival=context['festival'])
                art_q = models.Art.objects.filter(project_x = context['project'])

        context['artists'] = set(art.artist for art in art_q if art.artist.visible)
        context['breadcrumbs'] = self.breadcrumbs(context)
        random.shuffle(list(context['artists']))
        return context


class TreasureHuntArtists(PageMixin, BuildableListView):
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
        return [ ('/', 'Mykonos Biennale'), ('/artfestival/artists/', 'artists'), ('', artist.name )]


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
