import tagulous.views
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

from festivalA.models import Tag

#from filmfestival.rest_api import FilmView
sitemaps = {}



urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),   
	url(r'^googleb0df5a57edf84cfc\.html', TemplateView.as_view(template_name="googleb0df5a57edf84cfc.html")),      
	url(r'^robots\.txt$', TemplateView.as_view(template_name="robots.txt", content_type = 'text/plain')),                 
    url(r'^sitemap\.xml$', TemplateView.as_view(template_name="sitemap-x.xml", content_type = 'text/xml')), #sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    #url(r"^index.html$", HttpResponseRedirect('/2015-antidote/')),
    # Examples:
    #url(r"^$", TemplateView.as_view(template_name="index.html"), name="home"),
    #url(r"^2013-crises-and-paganism/$", TemplateView.as_view(template_name="2013-Crises-and-Paganism.html"), name="home"),
    #url(r"^mykonos-biennale/$", TemplateView.as_view(template_name="mykonos-biennale.html"), name="home"),
    url(r"^filmfestival/", include("filmfestival.urls")),

    url(r"^artfestival/", include("festival.urls")),  
#    url(r'^api/films', FilmView.as_view(), name='films'),
#    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', lambda x: HttpResponseRedirect('/2017-trans-allegoria/')),
    #url(r"(?P<processor>[A-Z]+:)*(?P<width>\d*)x(?P<height>\d*)(@(?P<resolution>\d+))*(Q(?P<quality>\d+))*(?P<image_url>\/.+)", 'imagelabs.views.process'),
 url(r'^photologue/', include('photologue.urls', namespace='photologue')),
    url(r"^", include("pages.urls")), 
                        url(
        r'^api/tags/$',
        tagulous.views.autocomplete,
        {'tag_model': Tag},
        name='festivalA_tag_autocomplete',
    ),
   #url(r"^index.html", lambda x: HttpResponseRedirect('/2015-antidote/')),
   #url(r"^2013-Crises-and-Paganism.html", lambda x: HttpResponseRedirect('/2013-crisis-and-paganism/')),
   #url(r"^mykonos_biennale.html", lambda x: HttpResponseRedirect('/mykonos-biennale/')),
)
urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
    )
