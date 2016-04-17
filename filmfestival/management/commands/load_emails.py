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



class Command(BaseCommand):
    help = '''Generate a `admin.py` file for the given app (models)'''

    def handle(self, *args, **kwargs):
        print time.ctime(), args, kwargs
        csvfile = open('emails-Y-R_3717028.csv', 'rb')
        filmreader = csv.DictReader(csvfile)
        for row in filmreader:
                try:
                    if not row['contact_email']:
                        print row
                    film = Film.objects.get(ref=row['ref'])
                    film.contact_email = row['contact_email']
                    film.save()
                except Film.DoesNotExist,e :
                    print row

                