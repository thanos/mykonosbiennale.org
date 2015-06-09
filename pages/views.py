from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render_to_response
import models

def page(request, slug):
    page = models.Page.objects.get(slug=slug)
    return render_to_response(page.template, {'current_page':page, 'pages': models.Page.objects.filter(visible=True)})
