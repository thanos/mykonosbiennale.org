from django.conf.urls import patterns, url

urlpatterns = patterns("",
    url(r"(?P<processor>[A-Z]+:)*(?P<width>\d*)x(?P<height>\d*)(@(?P<resolution>\d+))*(Q(?P<quality>\d+))*(?P<image>\/.+)", 'imagelabs.views.process'),

)


