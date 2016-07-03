from django.db import models
import os
from uuid import uuid4
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from polymorphic import PolymorphicModel

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
    css = models.TextField(blank=True, default='')
    javascript = models.TextField(blank=True, default='')
    
    def __unicode__(self):
        return self.name
    

    
    def participant(self):
        return self.panel_set.filter(visible=True)


    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Participant, self).save(*args, **kwargs)
    
    
    
    
    
    
    
class ParticipantRole(PolymorphicModel):
    participant = models.ForeignKey('Participant')
   
class Curator(ParticipantRole):
    field2 = models.CharField(max_length=10)
    
class Organiser(ParticipantRole):
    field2 = models.CharField(max_length=10)

class Artist(ParticipantRole):
    template = models.CharField(max_length=128, default='2015-artist.html')
    
    def get_absolute_url(self):
        return reverse('artist-detail', args=[self.slug]) 
    
    def artwork(self):
        try:
            return self.art_set.first().photo.url
        except: 
            pass 
        
        
class Dancer(ParticipantRole):
    field3 = models.CharField(max_length=10)

class Director(ParticipantRole):
    field3 = models.CharField(max_length=10)
    
 




    
        
class Art(models.Model):
    artist = models.ForeignKey(Artist)
    title = models.CharField(max_length=128, blank=True, default='')
    slug = models.SlugField(max_length=128)
    description = models.TextField(blank=True, default='')

    def __unicode__(self):
        return "{} {}".format(self.artist, self.title)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Art, self).save(*args, **kwargs)
