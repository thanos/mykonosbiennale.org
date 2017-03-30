from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from . import views


urlpatterns = patterns('',
    url(r'^(?P<slug>[^/.]+)/$', views.PageView.as_view(), name='page'),
    url(r".*Mykonos_Biennale_2015", views.Redirect2013View.as_view(), name='redirect_to_2013'),
)