from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from django.http import HttpResponseRedirect
#from filmfestival.rest_api import FilmView

urlpatterns = patterns('',
                       
    url(r"^index.html$", HttpResponseRedirect('/2015-antidote/')),
    # Examples:
    #url(r"^$", TemplateView.as_view(template_name="index.html"), name="home"),
    #url(r"^2013-crises-and-paganism/$", TemplateView.as_view(template_name="2013-Crises-and-Paganism.html"), name="home"),
    #url(r"^mykonos-biennale/$", TemplateView.as_view(template_name="mykonos-biennale.html"), name="home"),
    url(r'^admin/', include(admin.site.urls)),
    url(r"^filmfestival/", include("filmfestival.urls")),    
    url(r"^artfestival/", include("festival.urls")),  
#    url(r'^api/films', FilmView.as_view(), name='films'),
#    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', lambda x: HttpResponseRedirect('/2015-antidote/')),
    #url(r"(?P<processor>[A-Z]+:)*(?P<width>\d*)x(?P<height>\d*)(@(?P<resolution>\d+))*(Q(?P<quality>\d+))*(?P<image_url>\/.+)", 'imagelabs.views.process'),

    url(r"^", include("pages.urls")), 
   url(r"^index.html", lambda x: HttpResponseRedirect('/2015-antidote/')),
   url(r"^2013-Crises-and-Paganism.html", lambda x: HttpResponseRedirect('/2013-crisis-and-paganism/')),
   url(r"^mykonos_biennale.html", lambda x: HttpResponseRedirect('/mykonos-biennale/')),
)
# urlpatterns += patterns('',
#         url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
#             'document_root': settings.STATIC_ROOT,
#         }),
#     )
