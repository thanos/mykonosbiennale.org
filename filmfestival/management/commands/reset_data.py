# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import time,traceback
import re
import sys

import pprint
import optparse


from django.core.management.base import BaseCommand
from django.conf import settings


from sports import models

class Command(BaseCommand):
    help = '''Generate a `admin.py` file for the given app (models)'''

    def handle(self, *args, **kwargs):
        print time.ctime(), args, kwargs
        print 'deleting Hometowns'
        models.Hometown.objects.all().delete()
        models.School.objects.all().delete()
        models.Team.objects.all().delete()
        models.Scrape.objects.all().delete()
        models.Season.objects.all().delete()
        models.Coach.objects.all().delete()