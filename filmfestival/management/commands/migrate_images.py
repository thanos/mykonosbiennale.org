# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import time,traceback
import csv
import json
import re
import os
import sys
import csv
import pprint
import optparse

from django.core.files.storage import get_storage_class
from django.core.management.base import BaseCommand
from django.conf import settings

from django.utils.text import slugify
from filmfestival.models import Film
from festival.models import Artist

from pages.models import SlideShow, Slide, slide_show_image
from django.core.files import File
from django.core.files.base import ContentFile

def write_file(group, image):
    image_path =  os.path.join('images', group, os.path.basename(image.name))
    with open(image_path,'wb') as li:
      li.write(image.read())

class Command(BaseCommand):
    help = '''Generate a `admin.py` file for the given app (models)'''
    def handle(self, *args, **kwargs):
        print time.ctime(), args, kwargs
        t = time.time()
#         self.handle_slides()
#         self.handle_artist()
#         self.handle_film()
        self.load_art()
        print time.time() - t
        
        
    def load_art(self):
        loaded = json.load(open('art-x.json'))
        for row in loaded['rows']:
            print Artist.objects.get(pk=row['id'])
        
    def handle_slides(self, *args, **kwargs):
        print time.ctime(), args, kwargs
        t = time.time()
        rows =[]
        for slide in Slide.objects.all():
          rows.append( {
            'slide_show': slide.slide_show.title,
            'id': slide.pk,
            'title': slide.title,
            'content': slide.content,
            'image': slide.image.name if slide.image else None,
            'video': slide.video.name if slide.video else None,
            'css': slide.css,
            'visible':slide.visible,
            'order': slide.order
          })
          #if slide.image: write_file('slides', slide.image)
          #if slide.video: write_file('slides', slide.video)
        with open('slides-x.json', 'wb') as f:
          json.dump({'rows': rows}, f, indent=4, sort_keys=True)
        print time.time() - t
        
    def handle_artist(self, *args, **kwargs):
        print time.ctime(), args, kwargs
        t = time.time()
        rows =[]
        for artist in Artist.objects.all():
            print artist.pk
            #print '\tposter: ', artist.poster
            #print '\theadshot: ', artist.headshot
            row = {
                'id': artist.pk,
                'poster': artist.poster.name,
                'headshot': artist.headshot.name,
            }
            if artist.poster: write_file('artists/posters', artist.poster)
            if artist.headshot: write_file('artists/headshots', artist.headshot)
            projects = {}
            for art in artist.art_set.all():
                work = {
                        "id": art.pk,
                        "photo": art.photo.name,
                        "title": art.title,
                        "slug": art.slug,
                        "show": art.show,
                        "leader": art.leader,
                        "description": art.description,
                        "text": art.text,
                    }
                try:
                    projects[art.project.title].append(work)
                except KeyError:
                    projects[art.project.title] = [work]
                if art.photo: write_file('artists/art', art.photo)
            row['projects'] = projects
            rows.append(row)
        with open('art-x.json', 'wb') as f:
            json.dump({'rows': rows}, f, indent=4, sort_keys=True)
        print time.time() - t 
        
        

    def handle_film(self, *args, **kwargs):
        print time.ctime(), args, kwargs
        t = time.time()
        rows =[]
        for film in Film.objects.all():
          print film.pk,
          row = {
            'id': film.pk,
            'poster': film.poster.name,
          }
          #if film.poster: write_file('films/posters', film.poster)
          images = []
          print film.filmfestival_image_related.count()
          for image in film.filmfestival_image_related.all():
              images.append(image.image.name)
              #if image.image: write_file('films/stills', image.image)
          row['images'] = images
          rows.append(row)
        with open('films-x.json', 'wb') as f:
          json.dump({'rows': rows}, f, indent=4, sort_keys=True)
        print time.time() - t      
                