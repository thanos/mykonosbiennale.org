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

from filmfestival.models import Film

lists = [
    'directors',
    'screenwriters',
    'producers',
    'exec_producers',
    'co_producers',
    'cinematographers',
    'product_designers',
    'art_directors',
    'editors',
    'sound_editors',
    'composers',
    'screenings',
    'actors',
]


mappings = {'Facebook': 'facebook'}

class Command(BaseCommand):
    help = '''Generate a `admin.py` file for the given app (models)'''

    def handle(self, *args, **kwargs):
        print time.ctime(), args, kwargs
        csvfile = open('12396_20150608_ALL_G-Y-R_3705595.csv', 'rb')
        if True:
            print csvfile
            filmreader = csv.DictReader(csvfile)
            for row in filmreader:
                try:
                    row['slug'] = slugify(row['title'])
                    row['runtime'] = int(row['runtime'] if row['year'] else row['runtime'])
                    print row['ref'], row['title']
                    print Film.objects.get_or_create(ref = row['ref'], defaults = row)
                except:
                    print row
                    raise
                