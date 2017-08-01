from bakery.views import BuildableDetailView
from django.shortcuts import render_to_response
from django.views.generic import View,ListView

CURRENT_YEAR='2017'

import models
from festival.models import Festival
from pages.views import PageMixin, ProjectView, ProjectEntryView


def selected(request, what=models.Film.DRAMATIC_NIGHTS):
    qs = models.Film.objects.filter(status='SELECTED', film_type=what)
    qs.order_by('title')
    return render_to_response('selected.html', {'films': qs})

def send_emails(request):
    ids = request.GET['ids'].split(',')
    films = models.Film.objects.filter(pk__in=ids).order_by('title')
    return render_to_response('emails.html', {'films':films})#, content_type='text/ascii')


class SelectedView(View):
    def get(self, request, what=models.Film.DRAMATIC_NIGHTS):
        qs = models.Film.objects.filter(status='SELECTED', film_type=what)
        qs.order_by('title')
        return render_to_response('selected.html', {'films': qs})


class FilmList(ListView):
    sub_title = ''
    film_type = models.Film.DRAMATIC_NIGHTS
    queryset = models.Film.objects.filter(status='SELECTED').order_by('title')

    def get_queryset(self):
        queryset = super(FilmList, self).get_queryset()
        queryset = queryset.filter(project__festival__year=int(self.kwargs.get('year', CURRENT_YEAR)))

        return queryset

    def breadcrumbs(self, context):
        pass

    def getObject(self, context):
        return context['object_list']

    def get_context_data(self, **kwargs):
        context = super(FilmList, self).get_context_data(**kwargs)
        context['breadcrumbs'] = self.breadcrumbs(context)
        context['festival'] = Festival.objects.filter(year=int(self.kwargs.get('year', CURRENT_YEAR))).first()
        context['seo'] = self.seo(context)
        return context

    def seo(self, context):

        festival = context['festival']
        seo_data = {
            'title': festival.label,
            'sub_title': '',
            'description': 'The list of films presented in this years festival, {}'.format(
                festival),
            'image': 'http://mykonosbiennale.org/static/images/mykonos-biennale-logo.png',
        }
        return seo_data

class FilmProjectList(ProjectView):
    sub_title =''
    film_type = models.Film.DRAMATIC_NIGHTS
    queryset = models.Film.objects.filter(status='SELECTED').order_by('title')
    
    def get_queryset(self):
        queryset = super(FilmProjectList, self).get_queryset()
        if 'project' in self.kwargs:
            queryset = queryset.filter(project__slug =self.kwargs['project'])
        queryset = queryset.filter(project__festival__year=int(self.kwargs.get('year', CURRENT_YEAR)))
        
        return queryset
    
    def getObject(self, context):

        return context['object_list']
    
    # def get_context_data(self, **kwargs):
    #     kwargs['project'] = models.Project.objects.get(slug=self.kwargs['project'],
    #                                                     festival__year=int(self.kwargs.get('year', CURRENT_YEAR)))
    #     context =  super(FilmList, self).get_context_data(**kwargs)
    #
    #     context['seo'] = self.seo(context)
    #     return context

    
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
    
    
    
    
    
class FilmDetail(ProjectEntryView):
    model = models.Film
    def seo(self, context):
        film = self.getObject(context)
        seo_data =  {
            'title': '{} - {}'.format(film.project, film.title),
            'description': film.log_line,
            'url': film.get_absolute_url(),
            'description_155': film.log_line[:155],
            'description_200': film.log_line[:200],
            'description_300': film.log_line[:300],
        }
        if film.poster:
            seo_data['image'] = film.poster.url
        return seo_data
    
    def breadcrumbs(self, context):
        film = self.getObject(context)
        festival = film.project.festival
        return [('/', festival), ('/filmfestival/%s/%s/' %( festival.year, film.project.slug),  film.project.title), ('', film.title )]
    
    
    
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
