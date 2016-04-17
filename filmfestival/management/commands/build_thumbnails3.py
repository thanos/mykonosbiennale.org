# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import time,traceback
import re
import sys
import csv
import pprint
import optparse


from django.core.management.base import BaseCommand
from django.conf import settings

from django.utils.text import slugify

from filmfestival.models import Film, Image



class Command(BaseCommand):
    help = '''Generate a `admin.py` file for the given app (models)'''

    def handle(self, *args, **kwargs):
        print time.ctime(), args, kwargs
        t = time.time()
#         for film in Film.objects.exclude(poster=None):
#             poster = film.poster
#             if poster:
#                 try:
#                     if film.title in ('The Tree of Numbers','Noise','Strawberries', 'Acid Make-Out'): 
#                         print '??? skipping', film.title
#                         continue
#                     sz =poster.width * poster.height
#                     if  sz < 89478485:
#                            print film.poster_thumbnail.url
#                     else:
#                         print '>>>>>'
#                         print '>>>>> warning', film.title, sz
#                         print '>>>>'
#                 except:
#                     print film.title
#                     traceback.print_exc()
#         print time.time() - t
        
        
#         for film in Film.objects.exclude(poster=None):
#             poster = film.poster
#             if poster:
#                 try:
#                     if film.title in ('The Tree of Numbers','Noise','Strawberries', 'Acid Make-Out'): 
#                         print '??? skipping', film.title
#                         continue
#                     sz =poster.width * poster.height
#                     if  sz < 89478485:
#                            print film.poster_for_download.url
#                     else:
#                         print '>>>>>'
#                         print '>>>>> warning', film.title, sz
#                         print '>>>>'
#                 except:
#                     print film.title
#                     traceback.print_exc()
#         print time.time() - t
        
        
        
        
        t = time.time()
        for image in Image.objects.exclude(image=None):
            if image.image:
                try:
                    if str(image.image) in (
                        'images/mykonos-biennale-2015-film-festival-257k-257k-eva-colmers-Screenshot-0.jpg',
                        'images/mykonos-biennale-2015-film-festival-257k-257k-eva-colmers-Screenshot-1.jpg',
                    ): 
                        print >> sys.stderr, '??? skipping', image.image
                        continue
                    sz =image.image.width * image.image.height
                    if  sz < 89478485:
                        print 'image:', image.image
                        print image.image_thumbnail.url
                    else:
                        print >> sys.stderr, '>>>>>'
                        print >> sys.stderr, '>>>>> BIG  warning', image.title, sz
                        print >> sys.stderr, '>>>>'
                except:
                    print image.title
                    traceback.print_exc()
                
        print time.time() - t

            
#         t = time.time()
#         for image in Image.objects.exclude(image=None):
#             if image.image:
#                 try:
#                     if str(image.image) in (
#                         'images/mykonos-biennale-2015-film-festival-257k-257k-eva-colmers-Screenshot-0.jpg',
#                         'images/mykonos-biennale-2015-film-festival-257k-257k-eva-colmers-Screenshot-1.jpg',
#                     ): 
#                         print >> sys.stderr, '??? skipping', image.image
#                         continue
#                     sz =image.image.width * image.image.height
#                     if  sz < 89478485:
#                            print 'image:', image.image
#                            print image.image_for_download.url
#                     else:
#                         print >> sys.stderr, '>>>>>'
#                         print >> sys.stderr, '>>>>> BIG  warning', image.title, sz
#                         print >> sys.stderr, '>>>>'
#                 except IOError:
#                     print image.title
#                     traceback.print_exc()
#                     return
#                 except:
#                     print image.title
#                     traceback.print_exc()
#         print time.time() - t       
            
            
            
                