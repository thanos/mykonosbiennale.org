from django.shortcuts import render


from django.http import Http404
from django.shortcuts import render_to_response
from django.views.generic import ListView,DetailView
from pages.views import PageMixin,ListMixin
from django.views.generic import View
from bakery.views import BuildableMixin, BuildableRedirectView, BuildableListView, BuildableDetailView
from festival.models import Project

import models

def selected(request, what=models.Film.DRAMATIC_NIGHTS):
    qs = models.Film.objects.filter(status='SELECTED', film_type=what)
    qs.order_by('title')
    return render_to_response('selected.html', {'films': qs})

def send_emails(request):
    ids = request.GET['ids'].split(',')
    films = models.Film.objects.filter(pk__in=ids).order_by('title')
    return render_to_response('emails.html', {'films':films})#, content_type='text/ascii')


class SelectedView(View, BuildableMixin):
    def get(self, request, what=models.Film.DRAMATIC_NIGHTS):
        qs = models.Film.objects.filter(status='SELECTED', film_type=what)
        qs.order_by('title')
        return render_to_response('selected.html', {'films': qs})


class FilmList(ListView, ListMixin):
    sub_title =''
    film_type = models.Film.DRAMATIC_NIGHTS
    queryset = models.Film.objects.filter(status='SELECTED').order_by('title')
    
    def get_queryset(self):
        queryset = super(FilmList, self).get_queryset()
        queryset = queryset.filter(project__slug =self.kwargs['project'])
        queryset = queryset.filter(project__festival__year=int(self.kwargs.get('year', '2015')))
        
        return queryset
    
    def getObject(self, context):
        return context['object_list']
    
    def get_context_data(self, **kwargs):
        context =  super(FilmList, self).get_context_data(**kwargs)
        context['project'] = Project.objects.get(slug=self.kwargs['project'], festival__year=int(self.kwargs.get('year', '2015')))
        context['seo'] = self.seo(context)
        return context
    
    def seo(self, context):
        x =  super(FilmList,self).seo(context)
        project = context['project']
        x.update({
            'title': 'Mykonos Biennale 2015 - {}'.format(project.title),
            'sub_title': project.title,
            'description': 'The list of films presented in {}'.format(project.title),
        })
        return x
    
class DramaticNightsFilms(FilmList):
    film_type = models.Film.DRAMATIC_NIGHTS
    sub_title = 'Dramatic Nights'
    queryset = models.Film.objects.filter(status='SELECTED').exclude(film_type=models.Film.VIDEO_GRAFITTI).exclude(film_type=models.Film.DANCE).order_by('title')
class VideoGraffitiFilms(FilmList):
    film_type = models.Film.VIDEO_GRAFITTI
    sub_title = 'Video Graffiti'
    queryset = models.Film.objects.exclude(film_type=models.Film.DRAMATIC_NIGHTS).exclude(film_type=models.Film.DOCUMENTARY).filter(status='SELECTED').order_by('title')

class DocumentaryFilms(FilmList):
    film_type = models.Film.DOCUMENTARY
    sub_title = 'Documentary'
    queryset = models.Film.objects.filter(status='SELECTED', film_type= film_type).order_by('title')

class DanceFilms(FilmList):
    film_type = models.Film.DANCE
    sub_title = 'Dance'
    queryset = models.Film.objects.filter(status='SELECTED', film_type= film_type).order_by('title')
          

class WhoIsComing(FilmList):
    film_type = models.Film.DANCE
    sub_title = 'Who is Comming'
    template_name ='filmfestival/who-is-coming.html'
    queryset = models.Film.objects.filter(present=True).order_by('title')
    
class MissingMedia(FilmList):
    film_type = models.Film.DANCE
    sub_title = 'Missing Media'
    template_name ='filmfestival/missing-media.html'
    queryset = models.Film.objects.filter(status='SELECTED', projection_copy=False).order_by('title')
    
    
    
    
    
class FilmDetail(PageMixin, BuildableDetailView):
    model = models.Film
    def seo(self, context):
        film = self.getObject(context)
        x = super(FilmDetail,self).seo(context) 
        x.update({
            'title': 'Mykonos Biennale 2015 - {}'.format(film.title),
            'description': film.synopsis,
        })
        if film.poster:
            x['image'] = film.poster.url    
            return x
    
    def breadcrumbs(self, context):
        film = self.getObject(context)
        return [('/', '2015 - Antidote'), ('/filmfestival/films/', 'films'), ('', film.title )]   
    
    
    
class ProgramDetail(PageMixin, BuildableDetailView):
    model = models.Program
    def seo(self, context):
        program = self.getObject(context)
        x = super(ProgramDetail,self).seo(context) 
        x.update( {
            'title': 'Mykonos Biennale 2015 - {} - Program'.format(program.title),
            'description': ' The program and times of films  presented in {}'.format(program.title),
            'url': "/artfestival/artists", 
        })
        return x
