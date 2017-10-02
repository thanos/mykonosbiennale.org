from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page

import views
urlpatterns = patterns('',
	url(r'^art/$', views.ProjectDetail.as_view(), {'slug': 'all'}, name='art'), 
	url(r'^art/(?P<year>[0-9]+)/$', views.ProjectDetail.as_view(), {'slug': 'all'}, name='art'), 				   
	url(r'^art/(?P<slug>[^/]+)/$', views.ProjectDetail.as_view(), name='project'), 
	url(r'^art/(?P<year>[0-9]+)/(?P<slug>[^/]+)/$', views.ProjectDetail.as_view(), name='project'), 	
					  
	
	url(r'^treasure-hunt-artists/$', views.TreasureHuntArtists.as_view(), name='treasure-hunt'),
	url(r'^(?P<slug>[^/]+)/artists/$', views.ArtistList.as_view(), name='artist-list'),
	url(r'^artists/$', views.ArtistList.as_view(), name='artist-list'),
	url(r'^artists/(?P<year>[0-9]+)/$', views.ArtistList.as_view(), name='artist-list'),
	url(r'^artists/(?P<year>[0-9]+)/(?P<project>[^/]+)/$', views.ArtistList.as_view(), name='artist-list-by-project'),
	url(r'^artist/(?P<year>[0-9]+)/(?P<slug>[^/]+)/$', views.ArtistDetail.as_view(), name='artist-detail'),
	url(r'^artist/(?P<slug>[^/]+)/$', views.ArtistDetail.as_view(), name='artist-detail'),

) 
