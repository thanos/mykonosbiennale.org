from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page

import views
urlpatterns = patterns('',
    url(r'^artists/$', views.ArtistList.as_view(), name='artist-list'),  
    url(r'^artist/(?P<slug>[^/]+)/$', cache_page(60 * 15)(views.ArtistDetail.as_view()), name='artist-detail'),
) 
