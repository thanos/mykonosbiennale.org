from django.shortcuts import render


from django.http import Http404
from django.shortcuts import render_to_response
from django.views.generic import ListView,DetailView


import models

def selected(request, what=models.Film.DRAMATIC_NIGHTS):
    qs = models.Film.objects.filter(status='SELECTED', film_type=what)
    qs.order_by('title')
    return render_to_response('selected.html', {'films': qs})




class FilmList(ListView):
    film_type = models.Film.DRAMATIC_NIGHTS
    queryset = models.Film.objects.filter(status='SELECTED').order_by('title')
    
class DramaticNightsFilms(FilmList):
    film_type = models.Film.DRAMATIC_NIGHTS
    queryset = models.Film.objects.filter(status='SELECTED', film_type= film_type).order_by('title')

class VideoGraffitiFilms(FilmList):
    film_type = models.Film.VIDEO_GRAFITTI
    queryset = models.Film.objects.filter(status='SELECTED', film_type= film_type).order_by('title')

class DocumentaryFilms(FilmList):
    film_type = models.Film.DOCUMENTARY
    queryset = models.Film.objects.filter(status='SELECTED', film_type= film_type).order_by('title')
        
        
class FilmDetail(DetailView):
    model = models.Film
    
class ProgramDetail(DetailView):
    model = models.Program 
