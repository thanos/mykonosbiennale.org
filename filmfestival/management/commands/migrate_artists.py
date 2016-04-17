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

from festival import models as festival_model
from festivalA import models as festivalA_model

class Command(BaseCommand):
    help = '''Generate a `admin.py` file for the given app (models)'''

    def handle(self, *args, **kwargs):
        print time.ctime(), args, kwargs
        festivalA_model.Artist.objects.all().delete()
        title='Antidote'
        festival, created = festivalA_model.Festival.objects.get_or_create(title=title, slug = slugify(title), year=2015)
        
        for o_artist in festival_model.Artist.objects.filter(visible=True):
            participant, created = festivalA_model.Participant.objects.get_or_create(
                name =  o_artist.name, defaults= dict(
                slug = o_artist.slug,
                bio = o_artist.bio,
                statement =    o_artist.statement,
                email = o_artist.email,
                country = o_artist.country,
                phone = o_artist.phone,
                homepage = o_artist.homepage,
                visible = o_artist.visible,
                template = o_artist.template,
                css = o_artist.css,
                headshot =  o_artist.headshot,
                tags = '2015,artist',
                javascript = o_artist.javascript))
            artist, created = festivalA_model.Artist.objects.get_or_create(participant  = participant)
            
            title='Treasure Hunt'
            project, created = festivalA_model.Project.objects.get_or_create(title=title,slug = slugify(title), festival=festival)
            
            name='Delos'
            location, created = festivalA_model.Location.objects.get_or_create(name=name,slug = slugify(name))
            
            title='Treasure Hunt in Delos'
            event, created = festivalA_model.Event.objects.get_or_create(title=title,slug = slugify(title), location=location, project =project)  
            #artist.headshot.save(o_artist.name , o_artist.headshot.read(), save=True)
            count = 0
            for art in o_artist.art_set.all():
                print art, art.photo
                new_art, created = festivalA_model.Art.objects.get_or_create(
                    artist = artist,
                    title = art.title,
                    slug = art.slug + '-%d' % count,
                    description = art.description,
                    photo = art.photo,
                    tags = '"2015/%s"' % event.title
                    )
                new_art.events.add(event)
                new_art.save()
                count +=1