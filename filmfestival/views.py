from django.shortcuts import render


from django.http import Http404
from django.shortcuts import render_to_response
from django.views.generic import ListView,DetailView

import models


from pages.views import PageMixin,ListMixin


def selected(request, what=models.Film.DRAMATIC_NIGHTS):
    qs = models.Film.objects.filter(status='SELECTED', film_type=what)
    qs.order_by('title')
    return render_to_response('selected.html', {'films': qs})




class FilmList(ListMixin,ListView):
    film_type = models.Film.DRAMATIC_NIGHTS
    queryset = models.Film.objects.filter(status='SELECTED').order_by('title')
    def getObject(self, context):
        return context['object_list']
    def seo(self, context):
        x =  super(FilmList,self).seo(context)
        x.update({
            'title': 'Mykonos Biennale 2015 - {}'.format(self.sub_title),
            'sub_title': self.sub_title,
            'description': 'The list of presented in {}'.format(self.sub_title),
        })
        return x
    
class DramaticNightsFilms(FilmList):
    film_type = models.Film.DRAMATIC_NIGHTS
    sub_title = 'Dramatic Nights'
    queryset = models.Film.objects.filter(status='SELECTED', film_type= film_type).order_by('title')

class VideoGraffitiFilms(FilmList):
    film_type = models.Film.VIDEO_GRAFITTI
    sub_title = 'Video Graffiti'
    queryset = models.Film.objects.exclude(film_type=models.Film.DRAMATIC_NIGHTS).filter(status='SELECTED').order_by('title')

class DocumentaryFilms(FilmList):
    film_type = models.Film.DOCUMENTARY
    sub_title = 'Documentary'
    queryset = models.Film.objects.filter(status='SELECTED', film_type= film_type).order_by('title')

class DanceFilms(FilmList):
    film_type = models.Film.DANCE
    sub_title = 'Dance'
    queryset = models.Film.objects.filter(status='SELECTED', film_type= film_type).order_by('title')
          
        
class FilmDetail(PageMixin, DetailView):
    model = models.Film
    def seo(self, context):
        film = self.getObject(context)
        print super(FilmDetail,self).seo(context)
        x = super(FilmDetail,self).seo(context) 
        x.update({
            'title': 'Mykonos Biennale 2015 - {}'.format(film.title),
            'description': 'The list of presented in {}'.format(film.synopsis),
        })
        return x
    
    
    
    
class ProgramDetail(PageMixin, DetailView):
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