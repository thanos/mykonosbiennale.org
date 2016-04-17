from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page

import views
urlpatterns = patterns('',
	url(r'^art/$', views.ArtList.as_view(), name='art'), 
	 url(r'^treasure-hunt-artists/$', views.TreasureHuntArtists.as_view(), name='treasure-hunt'),  
    url(r'^artists/$', views.ArtistList.as_view(), name='artist-list'),  
    url(r'^artist/(?P<slug>[^/]+)/$', views.ArtistDetail.as_view(), name='artist-detail'),
) 
