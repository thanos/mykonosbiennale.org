from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from django.http import HttpResponseRedirect
from filmfestival.rest_api import FilmView

urlpatterns = patterns('',
    # Examples:
    #url(r"^$", TemplateView.as_view(template_name="index.html"), name="home"),
    #url(r"^2013-crises-and-paganism/$", TemplateView.as_view(template_name="2013-Crises-and-Paganism.html"), name="home"),
    #url(r"^mykonos-biennale/$", TemplateView.as_view(template_name="mykonos-biennale.html"), name="home"),
    url(r'^admin/', include(admin.site.urls)),
    url(r"^filmfestival/", include("filmfestival.urls")),    
    url(r"^artfestival/", include("festival.urls")),  
    url(r'^api/films', FilmView.as_view(), name='films'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', lambda x: HttpResponseRedirect('/2015-antidote/')),
    url(r"^", include("pages.urls")),           
)
# urlpatterns += patterns('',
#         url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
#             'document_root': settings.STATIC_ROOT,
#         }),
#     )