# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import time,traceback
import re
import sys
import csv
import pprint
import optparse

from django.core.files.storage import get_storage_class
from django.core.management.base import BaseCommand
from django.conf import settings

from django.utils.text import slugify

from pages.models import Slide, slide_show_image
from django.core.files import File
from django.core.files.base import ContentFile

class Command(BaseCommand):
    help = '''Generate a `admin.py` file for the given app (models)'''

    def handle(self, *args, **kwargs):
        print time.ctime(), args, kwargs
        t = time.time()
        for slide in Slide.objects.exclude(image=None):
            if slide.image:
                try:
                    sz =slide.image.width * slide.image.height
                    if  sz < 89478485:
                        #print 'image:', slide.image
                        with open('static/images/XXX.jpg','wb') as li:
                            li.write(slide.image.read())
                            
                        
                        print 'OLD', slide.pk
                        #print 'OLD', slide.image.url
                        #print dir(slide.image)
                        name =  slide_show_image(slide, 'XXX.jpg')
#                         print name
                        #s = Slide.objects.get(order=999)
#                         print get_storage_class()
#                         storage, path = s.image.storage, s.image.name
#                         storage.delete(path)
                        slide.image.save(name, File(open('static/images/XXX.jpg', 'rb')))
                        #s.image.close()
                        #s.image= None
                        slide.save()
                        #print slide.image
#                         file = get_storage_class()().open(name, 'w')
#                         file.write(ContentFile(open('static/images/XXX.jpg', 'rb')))
#                         file.close()
                        #print slide.image.url
                        #print slide.image_to_use.url
                    else:
                        print >> sys.stderr, '>>>>>'
                        print >> sys.stderr, '>>>>> BIG  warning', slide.title, sz
                        print >> sys.stderr, '>>>>'
                except:
                    print slide.pk
                    traceback.print_exc()
                
        print time.time() - t
           
                