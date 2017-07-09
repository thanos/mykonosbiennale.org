import os
from django.db import models
from django.utils.text import slugify
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django_countries.fields import CountryField
from model_utils.managers import InheritanceManager
from model_utils.models import StatusModel
from model_utils import Choices

from versatileimagefield.fields import VersatileImageField
import tagulous.models
from phonenumber_field.modelfields import PhoneNumberField



class Tag(tagulous.models.TagTreeModel):
    class TagMeta:
        force_lowercase = True

# Create your models here.
class Basics(models.Model):
    name = models.CharField(max_length=100)
    sort_by = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(max_length=200, null=True, blank=True)
    text = models.TextField(default='', blank=True)
    tags = tagulous.models.TagField(to=Tag, default='',  blank=True)
    #albumn = models.ForeignKey('Album', null=True, blank=True)
    class Meta:
        abstract = True
        ordering = ['sort_by']
        
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return '/{}/'.format(self.slug)
    


    def save(self, *args, **kwargs):
        self.name = ' '.join(self.name.strip().split())
        if not self.sort_by:
                self.sort_by = self.name
        if not self.slug:
            self.slug = slugify(self.sort_by)
        super(Basics, self).save(*args, **kwargs)

class Album(Basics):
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey()
    media = models.ManyToManyField('Media', related_name='album')
#     @classmethod
#     def get_for(cls, what):
#         ct = ContentType.objects.get_for_model(what)
#         return cls.objects.filter(content_type=ct, object_id=what.id)
    
    
class Media(Basics):
    image = VersatileImageField('image', upload_to='material/', null=True, blank=True)
    video  = models.FileField (upload_to='material/',  max_length=256, null=True, blank=True)
    src = models.TextField(default='',  blank=True)

    

    

    
    
class Festival(Basics):
    year = models.IntegerField(default= 2015)
    class Meta:
        ordering = ['-year']
        
    def get_absolute_url(self):
        return '/{}/'.format(self.slug)
          
    def __unicode__(self):
        return "{} - {}".format(self.year, self.name)
    
    def save(self, *args, **kwargs):
        self.slug = "{}-{}".format(self.year, slugify(self.name))
        super(Basics, self).save(*args, **kwargs)   
    
class Project(Basics):
    pass

class FestivalProject(Basics):
    festival = models.ForeignKey(Festival, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    def clean(self):
        if not self.text:
            self.text =  self.project.text
        
        tags = set(self.tags.get_tag_list()
                   + self.festival.tags.get_tag_list()
                   + self.project.tags.get_tag_list())
        self.tags.set_tag_list(tags)
        self.tags.save()
        return super(FestivalProject, self).clean()
    
    def get_absolute_url(self):
        return '/{}/{}/'.format(self.festival.slug, self.project.slug)
          
    def __unicode__(self):
        return "{} - {}".format(self.festival, self.name)

    
class Participant(Basics):
    email = models.EmailField(blank=True, default='')
    country = CountryField(blank=True, default='')
    phone = PhoneNumberField(blank=True, default='')  
    statement =    models.TextField( blank=True, default='')
    facebook = models.CharField(max_length=100, blank=True, default='')
    twitter = models.CharField(max_length=100, blank=True, default='')
    instagram = models.CharField(max_length=100, blank=True, default='')
    headshot =  VersatileImageField(upload_to='material/', null=True, blank=True)
    album = models.ForeignKey('Album', null=True, blank=True)
    homepage = models.URLField(blank=True, default='')
    
    @property
    def bio(self):
        return self.text
    
    @bio.setter
    def bio(self, text):
        self.text = text
        
    def headshot_tag(self):
      return u'<img height="75" src="%s" />' % self.headshot.url if self.headshot else ''
    headshot_tag.short_description = 'headshot'
    headshot_tag.allow_tags = True
    
class Participation(models.Model):
    festival_project = models.ForeignKey(FestivalProject, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    objects = InheritanceManager()
    
    def __unicode__(self):
        return "{} - {}".format(self.festival_project, self.participant)

    def headshot_tag(self):
      return self.participant.headshot_tag()
    headshot_tag.short_description = 'headshot'
    headshot_tag.allow_tags = True
    
#     def save(self, *args, **kwargs):
#         if not self.text:
#             self.text =  self.project.text
#         super(Basics, self).save(*args, **kwargs)
#         tags = set(self.tags.get_tag_list()
#                    + self.festival_project.tags.get_tag_list()
#                    + self.participant.tags.get_tag_list())
#         self.tags.set_tag_list(tags)
#         self.tags.save()
    
class Artist(Participation):
    artwork =  models.ManyToManyField('Art', related_name='artist', null=True, blank=True)
    def __unicode__(self):
        return "{} {} {}".format(self.participant.name, self.festival_project, self.artwork.first())
    
    def art(self):
      return self.artwork.first()
    art.short_description = 'art'
    art.allow_tags = True 
    
class FilmDirector(Participation):
    films =  models.ManyToManyField('Film', related_name='directors')
    
class Organizer(Participation):
    pass



class Art(Album):
    pass


class Film(Basics):
    class Meta:
        ordering = ['ref']

    FILM_SOURCES = Choices('withoutabox', 'filmfreeway', 'other')
    film_source = models.CharField(choices=FILM_SOURCES, default=FILM_SOURCES.withoutabox, max_length=20)
    ref = models.CharField(max_length=30)
    
    ENTRY_STATUS = Choices('selected', 'undecided', 'no')
    entry_status = models.CharField(choices=ENTRY_STATUS, default=ENTRY_STATUS.undecided, max_length=20)
    FILM_TYPES = Choices('dance', 'documentary', 'short', 'art_video')
    film_type = models.CharField(choices=FILM_TYPES, default=FILM_TYPES.short, max_length=20)   

    original_title = models.CharField(max_length=200,blank=True, default='')
    sub_by = models.CharField(max_length=128, default='')
    contact_email = models.EmailField(blank=True, default='')
    contact_phone =  PhoneNumberField(blank=True, default='') 
    posted_on_facebook = models.BooleanField(default=False)
    subtitles = models.BooleanField(default=False)
    language= models.CharField(max_length=128,blank=True, default='')
    actors = models.TextField(blank=True, default='')
    year = models.CharField(max_length=4)
    runtime = models.IntegerField()
    country = models.TextField(blank=True, default='')
    
    projection_copy = models.BooleanField(default= False)
    projection_copy_url = models.URLField(blank=True, default='')
    
    coming = models.BooleanField(default= False)
    present = models.BooleanField(default= False)
    when = models.CharField(max_length=64,blank=True, default='')
    
    log_line = models.TextField(blank=True, default='')
    synopsis = models.TextField(blank=True, default='')
    synopsis_125 = models.TextField( blank=True, default='')
    synopsis_250 = models.TextField( blank=True, default='')
    first_time = models.CharField(max_length=164,  blank=True, default='') 
    twitter = models.CharField(max_length=164,  blank=True, default='')
    facebook = models.CharField(max_length=164,  blank=True, default='') 
    other_social_media = models.CharField(max_length=164,  blank=True, default='') 

    screenwriters = models.TextField(blank=True, default='')
    producers = models.TextField(blank=True, default='')
    exec_producers = models.TextField(blank=True, default='')
    co_producers = models.TextField(blank=True, default='')
    cinematographers = models.TextField(blank=True, default='')
    product_designers  = models.TextField(blank=True, default='')
    art_directors = models.TextField(blank=True, default='')
    editors = models.TextField(blank=True, default='')
    sound_editors = models.TextField(blank=True, default='')
    composers  = models.TextField(blank=True, default='')
    screenings  = models.TextField(blank=True, default='')
    url = models.URLField(blank=True, default='')

    genres = models.CharField(max_length=128, blank=True, default='')
    niches = models.CharField(max_length=256, blank=True, default='')
    info = models.TextField(blank=True, default='')
    directors_statement = models.TextField(blank=True, default='')
    production_notes = models.TextField(blank=True, default='')
    crew = models.TextField(blank=True, default='')
    
    poster = VersatileImageField(upload_to='posters/', null=True, blank=True)
        
    trailer_url = models.URLField(blank=True, default='')
    trailer_embed = models.TextField(blank=True, default='')
    trailer_video  = models.FileField (upload_to='material/',  max_length=256, null=True, blank=True)
    
    stills = models.OneToOneField(Album,  blank=True, null=True, related_name='film_of_stills')
    photos = models.OneToOneField(Album,  blank=True, null=True, related_name='film_of_photos') 
