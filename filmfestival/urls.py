from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from filmfestival import views
from django.views.decorators.cache import cache_page

urlpatterns = patterns('',
    url(r'^selected/(?P<what>[^/]+)/$', 'filmfestival.views.selected', name='selected'),
    url(r'^selected/$', 'filmfestival.views.selected', name='selected'),
    url(r'^films/$', views.FilmList.as_view(), name='film-list'),  
    url(r'^dramatic-nights/$', views.DramaticNightsFilms.as_view(), name='film-list'),
    url(r'^video-graffiti/$', views.VideoGraffitiFilms.as_view(), name='video-graffiti'),
    url(r'^documentaries/$', views.DocumentaryFilms.as_view(), name='documentaries'),
    url(r'^film/(?P<slug>[^/]+)/$', views.FilmDetail.as_view(), name='film-detail'),
    url(r'^program/(?P<slug>[^/]+)/$', views.ProgramDetail.as_view(), name='program'),
    #url(r'^film/(?P<slug>[^/]+)/$', cache_page(60 * 15)(views.FilmDetail.as_view()), name='film-detail'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)