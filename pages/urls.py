from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings




urlpatterns = patterns('',
    url(r'^(?P<slug>[^/.]+)/$', 'pages.views.page', name='page'),
)