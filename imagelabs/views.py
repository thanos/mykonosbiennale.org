# encoding: utf-8
import json, os

from django.http import HttpResponse
from django.views.generic import CreateView, DeleteView, ListView
from django.conf import settings
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404

from models import ProcessedImage
from  imagelabs import processor as ilabs_processor
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)
def process(request, image_url, processor=None, width=None, height=None, resolution=None, quality=100):
    print request, image_url, processor, width, height, resolution, quality
    try:
        processed_image = ProcessedImage.objects.get(source_image=image_url)
    except ProcessedImage.DoesNotExist:
        processed_image = ilabs_processor.process(image_url, processor, width, height, resolution, quality)
    return HttpResponsePermanentRedirect(processed_image.processed_image)
    
    
