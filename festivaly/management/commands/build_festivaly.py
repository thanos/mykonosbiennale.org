# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import time,traceback
import collections
import re
import os
import sys
import csv
import pprint
import optparse
from django.core.files.base import ContentFile
from nameparser import HumanName

from django.core.management.base import BaseCommand
from django.conf import settings

from django.utils.text import slugify

from festivaly import models as festivaly_models
from festival import models as festival_models
from filmfestival import models as filmffestival_models


class Command(BaseCommand):
    help = '''Generate a `admin.py` file for the given app (models)'''
  
    def handle(self, *args, **kwargs):
        self.process_filmdirectors()
#         for festival in festivaly_models.Festival.objects.all():
#             print (festival, festival.slug, festival.get_absolute_url())
#         for project in festivaly_models.Project.objects.all():
#             print (project, project.slug, project.get_absolute_url())
#         for festival_project in festivaly_models.FestivalProject.objects.all():
#             festival_project.save()
#             print (festival_project, festival_project.slug, festival_project.get_absolute_url())

        
#         f_2017 = festivaly_models.Festival.objects.get(year=2017)
#         for project in festivaly_models.Project.objects.all():
#             festival_project,_ =  festivaly_models.FestivalProject.objects.get_or_create(
#                     festival= f_2017,
#                     project = project,
#                     name = project.name,
#                     text = project.text)
                
#         for festival in festival_models.Festival.objects.all():
#             for projectx in festival.projectx_set.all():
#                 print festival, projectx

    def rec_2(self):
        for artist in festival_models.Artist.objects.all():
            try:
                festivaly_models.Participant.objects.get(name = artist.name)
            except:
                self.mirgate_artist(artist)
#         for festival_project in festivaly_models.FestivalProject.objects.filter(festival__year=2015):
#             ps = festival_models.ProjectSeason.objects.filter(project__title = festival_project.name).first()
#             if ps:
#                 print('found', ps, 'matches',festival_project)
                
#                 for artist in set([art.artist for art in ps.art_set.all()]):
                    
                    
    def purge(self):
        print festivaly_models.FilmDirector.objects.count()
        pees = [fd.participant for fd in  festivaly_models.FilmDirector.objects.all()]
        map(lambda x: x.delete(), pees)
        
    def process_names(self, text):
            for name in re.split("\s*[\/&,]\s*", text):
                yield HumanName(name)   
                
                

            # build album for each art piece
            
                    
            
#             album = {
#                             'festivalproject':festivalproject,
#                             'name': '{} - {}'.format(artist.name, work),
#                             'text': (works[work][0].description + '\n\n'+ works[work][0].text).strip(),
#                             'media':[]                          
#                         }
#                         artwork =  festivaly_models.Art.objects.create(
#                             name = album['name'],
#                             text = album['text']
#                         )    
            
        
    def migrate_film(self, old_film):
        #image = ContentFile(old_film.poster.read())
        dir_list = [str(name) for name in self.process_names(old_film.dir_by)]
        slug = slugify(old_film.title+'-'+' '.join(dir_list))
        festivalproject = festivaly_models.FestivalProject.objects.get(festival__year=2015, project__name={
                'Dramatic Nights': 'Dramatic Nights',
                'Video Graffiti': 'Video Graffiti',
                'Dance': 'Video Graffiti',
                'Video Grafitti': 'Video Graffiti',
                'Documentary': 'Dramatic Nights',
                    }[old_film.film_type])
        poster = None
        if old_film.poster:
            poster = ContentFile(old_film.poster.read())
            poster_name = 'mykonos-biennale-{}-{}-{}-post{}'.format(
                                        festivalproject.festival.slug,
                                        festivalproject.project.slug,
                                        old_film.slug,
                                        os.path.splitext(old_film.poster.name)[1]
                                    )
#         if old_film.trailer_video:
#               #trailer_video = ContentFile(old_film.trailer_video.read())
#             trailer_video_name = 'mykonos-biennale-{}-{}-{}-trailer{}'.format(
#                                         festivalproject.festival.slug,
#                                         festivalproject.project.slug,
#                                         old_film.slug,
#                                         os.path.splitext(old_film.poster.name)[1]
#                                    )   
        def synopsis(film):
            if film.log_line:
                return film.log_line
            elif film.synopsis_125:
                return film.synopsis_125
            elif film.synopsis_250:
                return film.synopsis_250
            else:
                return film.synopsis
        
        stills,_ = festivaly_models.Album.objects.get_or_create(
            name = "{} dir. by {}".format(old_film.title, ', '.join(dir_list)),
            defaults = dict(
                text = synopsis(old_film),
            )
        )
    
        film, created = festivaly_models.Film.objects.get_or_create(ref = old_film.ref, 
            defaults = dict(                                               
                film_source = old_film.source.lower(),
                ref = old_film.ref,
                entry_status = old_film.status.lower(),
                film_type = {
                    'Dramatic Nights': 'short',
                    'Video Graffiti': 'art_video',
                    'Video Grafitti': 'art_video',
                    'Dance': 'dance',
                    'Documentary': 'documentary',
                }.get(old_film.film_type),
                name = old_film.title,
                original_title = old_film.original_title,
                sub_by = old_film.sub_by,
                contact_email = old_film.contact_email,
                contact_phone = old_film.contact_phone,
                posted_on_facebook = old_film.posted_on_facebook,
                subtitles = old_film.subtitles,
                language = old_film.language,
                actors = old_film.actors,
                year = old_film.year,
                runtime = old_film.runtime,
                country = old_film.country,
                projection_copy = old_film.projection_copy,
                projection_copy_url = old_film.projection_copy_url,
                coming  = False,
                present = old_film.present,
                when = old_film.when,
                log_line = old_film.log_line,
                synopsis = old_film.synopsis,
                synopsis_125 = old_film.synopsis_125,
                synopsis_250 = old_film.synopsis_250,
                first_time = old_film.first_time,
                twitter = old_film.twitter,
                facebook = old_film.facebook,
                other_social_media = old_film.other_social_media,
                url = old_film.url,
                screenwriters = old_film.screenwriters,
                producers = old_film.producers,
                exec_producers = old_film.exec_producers,
                co_producers = old_film.co_producers,
                cinematographers = old_film.cinematographers,
                product_designers = old_film.product_designers,
                art_directors = old_film.art_directors,
                editors = old_film.editors,
                sound_editors = old_film.sound_editors,
                composers = old_film.composers,
                crew = old_film.crew,
                screenings = old_film.screenings,
                genres = old_film.genres,
                niches = old_film.niches,
                info = old_film.info,
                directors_statement = old_film.directors_statement,
                production_notes = old_film.production_notes,
                poster = poster,
                trailer_url = old_film.trailer_url,
                trailer_embed = old_film.trailer_embed,
                stills = stills
            )
        )

        for i,image in enumerate(old_film.filmfestival_image_related.all()):
            
            new_image = ContentFile(image.image.read())
            image_name = 'mykonos-biennale-{}-{}-{}-still{}{}'.format(
                                        festivalproject.festival.slug,
                                        festivalproject.project.slug,
                                        old_film.slug,
                                        ('-%d' % i) if i else '',
                                        os.path.splitext(image.image.name)[1]
                                    )
            media, created = festivaly_models.Media.objects.get_or_create(
                                name =  'still of {}{}'.format(film.name, (' (%d)' % i) if i else ''),
                                defaults = dict(
                                    text =  stills.text,
                                    image =  new_image,
                                )
                            )
            if created: film.stills.media.add(media)
        return film

    def process_films(self): 
        for director in festivaly_models.FilmDirector.objects.all():
            print director.participant.name
    
    def process_filmdirectors(self):
        def process_names(text):
            for name in re.split("\s*[\/&,]\s*", text):
                yield HumanName(name)
                
        
        for film in filmffestival_models.Film.objects.filter(status=filmffestival_models.Film.SELECTED):
            if  festivaly_models.Film.objects.filter(ref = film.ref).first():
                continue
            print film, film.film_type, film.dir_by
            new_film = self.migrate_film(film)        
            file_type= 'Video Graffiti' if film.film_type == 'Video Grafitti' else 'Dramatic Nights'
                
            festivalproject = festivaly_models.FestivalProject.objects.get(festival__year=2015, project__name=file_type)
            directors = [str(name) for name in process_names(film.dir_by)]
            #print '\t directors:', map(str, directors)
            submitter = HumanName(film.sub_by) if film.sub_by.strip() else None
            director_submitter = None
            if not submitter:
                director_submitter  = directors[0]
            elif submitter in directors:
                #print 'MATCH'
                director_submitter = directors[directors.index(submitter)]
            else:
                pass #print 'NO MATCH', submitter
            if director_submitter:
                pass
                #print '\t\t director submitted', director_submitter
                #print '\t\t ', film.contact_email
                #print '\t\t ', film.contact_phone
            for director in directors:
                if director == director_submitter:
                    participant,_ = festivaly_models.Participant.objects.get_or_create(name=str(director),
                                                                           defaults = dict(
                                                                           phone = film.contact_phone,
                                                                           email = film.contact_email
                                                                          ))
                else:
                    participant,_ = festivaly_models.Participant.objects.get_or_create(name=str(director))
                film_director, created = festivaly_models.FilmDirector.objects.get_or_create(participant=participant, festival_project=festivalproject)
                film_director.films.add(new_film)
                #return
                
#             if film.actors: print '\t actors:', [str(name) for name in process_names(film.actors)]
#             if film.producers: print '\t producers:', [str(name) for name in process_names(film.producers)]
#             if film.exec_producers: print '\t exec_producers:', [str(name) for name in process_names(film.exec_producers)]
#             if film.co_producers: print '\t co_producers:', [str(name) for name in process_names(film.co_producers)]
#             if film.cinematographers: print '\t cinematographers:', [str(name) for name in process_names(film.cinematographers)]    
#             if film.screenwriters: print '\t screenwriters:', [str(name) for name in process_names(film.screenwriters)]    
#             if film.editors: print '\t editors:', [str(name) for name in process_names(film.editors)]    
#             if film.sound_editors: print '\t sound_editors:', [str(name) for name in process_names(film.sound_editors)]    
#             if film.composers: print '\t composers:', [str(name) for name in process_names(film.composers)]    
#             if film.art_directors: print '\t art_directors:', [str(name) for name in process_names(film.art_directors)]    
#             if film.crew: print '\t crew:', [str(name) for name in process_names(film.crew)]    

    

    def list_festivals(self):                                                                 
        for festival in festivaly_models.Festival.objects.all():
            print (festival)
        
    def mirgate_artist(self, old_artist):
        participant = self.add_participant(old_artist)
        print participant
        artworks = collections.defaultdict(list)
        # collect the art by project
        for art in old_artist.art_set.all():
            festivalproject = festivaly_models.FestivalProject.objects.get(festival__year=2015, 
                                                                     project__name = art.project_x.project.title)
            artworks[festivalproject].append(art)
        for festivalproject in artworks:
            participation,_ =  festivaly_models.Artist.objects.get_or_create(festival_project=festivalproject, participant=participant)
            # collect the images by art piece
            works = collections.defaultdict(list)
            for photo in artworks[festivalproject]:
                works[photo.title].append(photo)
            # create album for each art piece
            for work in works:
                print '{} - {}'.format(participant.name, work)
                artwork, created =  festivaly_models.Art.objects.get_or_create(
                            name = '{} - {}'.format(participant.name, work),
                            text = (works[work][0].description + '\n\n'+ works[work][0].text).strip(),
                        )
                print artwork, created
                if created:
                    participation.artwork.add(artwork)
                    for  i,photo in enumerate(works[work]):
                                image = ContentFile(photo.photo.read())
                                image.name = 'mykonos-biennale-{}-{}-{}-{}{}{}'.format(
                                        festivalproject.festival.slug,
                                        festivalproject.project.slug,
                                        photo.artist.slug,
                                        photo.slug,
                                        ('-%d' % i) if i else '',
                                        os.path.splitext(photo.photo.name)[1]
                                    )
                                media, created = festivaly_models.Media.objects.get_or_create(
                                    name =  '{} - {}{}'.format(participant.name, photo.title,   ('(%d)' % i) if i else ''),
                                    defaults = dict(
                                        image =  image,
                                        text =  (photo.description + '\n\n'+ photo.text).strip(),
                                    )
                                )
                                print media, created
                                if created: artwork.media.add(media)
                    
#     def rec_art(self):
#         for artist in festivaly_models.Artist.objects.all():
#             if artist.artwork.first() == None:
#                 print artist
#                 old_artist = festival_models.Artist.objects.get(name=artist.participant.name)
#                 print 'old_artist:', old_artist
#                 projects = collections.defaultdict(list)
#                 for art in old_artist.art_set.all():
#                     projects[art.project_x].append(art)
#                 for project in projects:
#                     old_festival = project.festival
#                     festivalproject = festivaly_models.FestivalProject.objects.get(festival__year=old_festival.year, project__name=project.project.title)
#                     works = collections.defaultdict(list)
#                     for work in projects[project]:
#                         works[work.title].append(work)
#                     for work in works:

#                         album = {
#                             'festivalproject':festivalproject,
#                             'name': '{} - {}'.format(artist.name, work),
#                             'text': (works[work][0].description + '\n\n'+ works[work][0].text).strip(),
#                             'media':[]                          
#                         }
#                         artwork =  festivaly_models.Art.objects.create(
#                             name = album['name'],
#                             text = album['text']
#                         )
#                         artist.artwork.add(artwork)
#                         print 'artwork', artwork.pk
#                         for  i,p in enumerate(works[work]):
#                             image = ContentFile(p.photo.read())
#                             image.name = 'mykonos-biennale-{}-{}-{}-{}{}{}'.format(
#                                     festivalproject.festival.slug,
#                                     festivalproject.project.slug,
#                                     p.artist.slug,
#                                     p.slug,
#                                     ('-%d' % i) if i else '',
#                                     os.path.splitext(p.photo.name)[1]
#                                 )
#                             media = festivaly_models.Media.objects.create(
#                                 image =  image,
#                                 name =  '{} - {}'.format(artist.name, p.title),
#                                 text =  (p.description + '\n\n'+ p.text).strip(),
#                             )
#                             artwork.media.add(media)
#                             print 'media', media.pk
#                         print 'album', album

                            
                         
#                     print 'project- art:', project, projects[project]
#                     print '\t old project:', art, art.project_x
#                     festival = art.project_x.festival
#                     print '\t new project:', festivaly_models.FestivalProject.objects.get(festival__year=festival.year, project__name=art.project_x.project.title)
                
                #break
        
#         for i, art in enumerate(festivaly_models.Art.objects.all()):
#             print i, 'art', art, 'artist', [a.participant.name for a in art.artist.all()]
            
        
#     def migrate_2015_art(self):
#         artists = collections.defaultdict(list)
#         for ps in festival_models.ProjectSeason.objects.all():
#             for art in  ps.art_set.all():
#                 artists[art.artist.name].append((ps, art))
#         for a in artists:
#             print a, len(artists[a])
#             work = {}
#             work_images = collections.defaultdict(list)
#             if 'XXVenieri' not in a:
#                 for ips, art in artists[a]:
                    
# #                     print """
# #                         title: {title}
# #                         slug: {slug}
# #                         show: {show}
# #                         leader: {leader}
# #                         description: {description}
# #                         text: {text}
# #                         photo: {photo}
# #                     """.format(**vars(art))
#                     fp =  festivaly_models.FestivalProject.objects.get(festival__year=2015, name=ips.project.title)
#                     participant = festivaly_models.Participant.objects.get(name=a)
#                     artistp,_ =  festivaly_models.Artist.objects.get_or_create(festival_project=fp, participant=participant)
#                     work[(artistp, art.title)] = art
#                     work_images[(artistp, art.title)].append(art)
#                 #continue 
#                 for k in  work:
#                     artistp = k[0]
#                     art = work[k]
#                     text = art.description + '\n\n'+ art.text
#                     artwork,created  =  festivaly_models.Art.objects.get_or_create(
#                        name=art.title,
#                        defaults={ 'text': text.strip()}
#                     )
#                     print artwork,created
#                     if created: 
#                         artistp.artwork.add(artwork)
#                     for i, img in enumerate(work_images[k]):
#                         image = ContentFile(img.photo.read())
#                         image.name = 'mykonos-biennale-{}-{}-{}-{}{}{}'.format(
#                             k[0].festival_project.festival.slug,
#                             k[0].festival_project.project.slug,
#                             art.artist.slug,
#                             art.slug,
#                             ('-%d' % i) if i else '',
#                             os.path.splitext(img.photo.name)[1]
#                         )
#                         media = festivaly_models.Media.objects.create(
#                             image =  image,
#                             name =  artwork.name,
#                             text =  artwork.text
#                         )
#                         artwork.media.add(media)
               
     
#     def rec_2015_artists(self):
#         for artist in festival_models.Artist.objects.filter(visible=True):
#             try:
#                 found = festivaly_models.Participant.objects.get(name=artist.name)
#             except:
#                 print "not Found", artist.name
#                 for art in artist.art_set.all():
#                     print '\t', art, art.project_x.pk
#                 if not 'Lommel'  in artist.name:
#                     self.add_participant(artist)
    
    def add_participant(self, artist):
        print ('\t %s' % artist)
        if "The" in artist.name:
            sort_by = artist.name[4:].strip()
        else:
            name = HumanName(artist.name)
            sort_by = "{} {}".format(name.last, name.first).strip()
        headshot = artist.headshot
        participant,created = festivaly_models.Participant.objects.get_or_create(
                    name = artist.name,
                    defaults = dict(
                            sort_by = sort_by,
                            text = artist.bio,
                            statement = artist.statement,
                            email = artist.email,
                            country = artist.country,
                            phone = artist.phone,
                            homepage = artist.homepage,
                                )
                  )
        if created:
            if artist.headshot:
                participant.headshot = ContentFile(artist.headshot.read())
                participant.headshot.name = 'mykonos-biennale-artist-{}{}'.format(artist.slug, os.path.splitext(artist.headshot.name)[1])
                participant.save()
        print participant
        return participant
    
    



#     def add_artist(self, artist):
#         print ('\t %s' % artist)
#         if "The" in artist.name:
#             sort_by = artist.name[4:].strip()
#         else:
#             name = HumanName(artist.name)
#             sort_by = "{} {}".format(name.last, name.first).strip()
#         headshot = artist.headshot
#         if artist.headshot:
#             headshot = ContentFile(artist.headshot.read())
#             headshot.name = 'mykonos-biennale-artist-{}{}'.format(artist.slug, os.path.splitext(artist.headshot.name)[1])
#         new_artist  = festivaly_models.Artist.objects.get_or_create(
#                 festival_project = festival_project,
#                 participant = festivaly_models.Participant.objects.get_or_create(
#                     name = artist.name,
#                     defaults = dict(
#                             sort_by = sort_by,
#                             text = artist.bio,
#                             statement = artist.statement,
#                             email = artist.email,
#                             country = artist.country,
#                             phone = artist.phone,
#                             homepage = artist.homepage,
#                             headshot = headshot
#                                 )
#                   )[0]
#         )
#         print new_artist
#         return new_artist
                    
#     def mirgate_2015_artists(self):
#         for festival_project in festivaly_models.FestivalProject.objects.filter(festival__year=2015):
#             ps = festival_models.ProjectSeason.objects.filter(project__title = festival_project.name).first()
#             if ps:
#                 print('found', ps, 'matches',festival_project)
                
#                 for artist in set([art.artist for art in ps.art_set.all()]):
#                     print ('\t %s' % artist)
#                     if "The" in artist.name:
#                         sort_by = artist.name[4:].strip()
#                     else:
#                         name = HumanName(artist.name)
#                         sort_by = "{} {}".format(name.last, name.first).strip()
#                     headshot = artist.headshot
#                     if artist.headshot:
#                         headshot = ContentFile(artist.headshot.read())
#                         headshot.name = 'mykonos-biennale-artist-{}{}'.format(artist.slug, os.path.splitext(artist.headshot.name)[1])
#                     artist  = festivaly_models.Artist.objects.get_or_create(
#                             festival_project = festival_project,
#                             participant = festivaly_models.Participant.objects.get_or_create(
#                                 name = artist.name,
#                                 defaults = dict(
#                                         sort_by = sort_by,
#                                         text = artist.bio,
#                                         statement = artist.statement,
#                                         email = artist.email,
#                                         country = artist.country,
#                                         phone = artist.phone,
#                                         homepage = artist.homepage,
#                                         headshot = headshot
#                                             )
#                               )[0]
#                     )
#                     print artist
#             else:
#                  print('no match for',festival_project)
    

            
                