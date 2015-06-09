# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import time,traceback
import re
import sys

import pprint
import optparse


from django.core.management.base import BaseCommand
from django.conf import settings


from festival.models import headshotNamer,artNamer


class Command(BaseCommand):
    help = '''Generate a `admin.py` file for the given app (models)'''

    def handle(self, *args, **kwargs):
        print time.ctime(), args, kwargs
               
        class Artist:
            name='Mary M.D Harek'
            festival = '2015 - Antidote & All'
        print headshotNamer(Artist(), 'X.jepg')
        
        class Art:
            title ='A painting'
            artist = Artist()
        print artNamer(Art(), 'X.jepg')
