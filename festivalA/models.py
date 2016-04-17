from datetime import date
from django.db import models
import os
from uuid import uuid4
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from polymorphic import PolymorphicModel
from sorl.thumbnail import ImageField
import tagulous.models


class Festival(models.Model):
    class Meta:
        ordering = ['title']
    year = models.IntegerField(default= date.today().year)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    statement = models.TextField(default='')
    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Festival, self).save(*args, **kwargs)
        

        

def art_image_path(instance, filename):
    artist_slug = slugify(instance.artist.name)
    base, ext = os.path.splitext(filename)
    title_slug = slugify(instance.title)
    filename = 'mykonos-biennale-{}-{}-{}{}'.format('art', artist_slug, title_slug,ext)
    return os.path.join('images', filename)
        
def location_image_path(instance, filename):
    base, ext = os.path.splitext(filename)
    slug = slugify(instance.name)
    filename = 'mykonos-biennale-{}-{}{}'.format('location', slug, ext)
    return os.path.join('images', filename)

class Location(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image  = ImageField (upload_to=location_image_path,  max_length=256, blank=True, default=None)
    address =  models.TextField(blank=True, default='')
    url = models.URLField(blank=True, default='')
    embeded_map =  models.TextField(blank=True, default='')
    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('location', args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Location, self).save(*args, **kwargs)  
        
        

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    festival = models.ForeignKey('Festival')
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('project', args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)
        

class Event(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    project = models.ForeignKey('Project')
    location = models.ForeignKey('Location')
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('event', args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Event, self).save(*args, **kwargs)    
        
    
def participant_name(instance, filename):
    base, ext = os.path.splitext(filename)
    slug = slugify(instance.name)
    filename = 'mykonos-biennale-{}{}'.format( slug, ext)
    return os.path.join('images', filename)


class Tag(tagulous.models.TagTreeModel):
    class TagMeta:
        initial = "2013, 2013/artist, 2015"
        force_lowercase = True
        autocomplete_view = 'festivalA_tag_autocomplete'

class Participant(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    bio =    models.TextField( blank=True, default='')
    statement =    models.TextField( blank=True, default='')
    email = models.EmailField(blank=True, default='')
    country = CountryField(blank=True, default='')
    phone = PhoneNumberField(blank=True, default='')    
    homepage = models.URLField(blank=True, default='')
    visible = models.BooleanField(default=True)
    headshot  = models.ImageField (upload_to=participant_name, max_length=256, blank=True)
    template = models.CharField(max_length=128, default='2015-artist.html')
    css = models.TextField(blank=True, default='')
    javascript = models.TextField(blank=True, default='')
    tags = tagulous.models.TagField(to=Tag, default='')
    
    def __unicode__(self):
        return self.name

    def participant(self):
        return self.panel_set.filter(visible=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Participant, self).save(*args, **kwargs)
  
    
    
class Participation(PolymorphicModel):
    participant = models.ForeignKey('Participant')
    
    def __unicode__(self):
        return self.participant.name
    

class Curator(Participation):
    pass
    
class Organiser(Participation):
    pass

class Artist(Participation):

    def get_absolute_url(self):
        return reverse('artist-detail', args=[self.slug]) 

    def artwork(self):
        try:
            return self.art_set.first().photo.url
        except: 
            pass 

     
        
class Dancer(Participation):
    pass

class Director(Participation):
    pass
    
class FilmSubmitter(Participation):
    pass




    
        
class Art(models.Model):
    artist = models.ForeignKey(Artist)
    title = models.CharField(max_length=128, blank=True, default='')
    slug = models.SlugField(max_length=128)
    description = models.TextField(blank=True, default='')
    photo = models.ImageField (upload_to=art_image_path, max_length=256, blank=True)
    tags = tagulous.models.TagField(to=Tag, default='')
    events =  models.ManyToManyField('Event', related_name='art_exhibited')
    def __unicode__(self):
        return "{} {}".format(self.artist, self.title)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Art, self).save(*args, **kwargs)
        
    
    def artist_name(self):
        return self.artist.participant.name
    
    
    
class Film(models.Model):
    class Meta:
        ordering = ['ref']
    ref = models.CharField(max_length=30)    
    title = models.CharField(max_length=200)
    original_title = models.CharField(max_length=200,blank=True, default='')
    slug = models.SlugField(max_length=200)
    directed_by = models.ManyToManyField(Director, related_name='films_directed')
    synopsis = models.TextField(blank=True, default='')
    def __unicode__(self):
        return "{} ({})".format(self.title, self.ref)
        