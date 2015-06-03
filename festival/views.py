from django.shortcuts import render


from django.http import Http404
from django.shortcuts import render_to_response
from django.views.generic import ListView,DetailView


import models





class ArtistList(ListView):
    queryset = models.Artist.objects.filter(visible=True).order_by('name')
          
class ArtistDetail(DetailView):
    model = models.Artist
    
    
