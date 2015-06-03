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
        with open('wab-movies.csv', 'rb') as csvfile:
            filmreader = csv.DictReader(csvfile)
            for row in filmreader:
                try:
                    row['slug'] = slugify(row['title'])
                    row['runtime'] = int(row['runtime'] if row['year'] else row['runtime'])
                    Film.objects.create(**row)
                except:
                    print row
                    raise
                