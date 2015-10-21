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
    headshot  = models.ImageField (upload_to=headshotNamer, max_length=256, blank=True)
    bio =    models.TextField( blank=True, default='')
    statement =    models.TextField( blank=True, default='')
    email = models.EmailField(blank=True, default='')
    country = CountryField(blank=True, default='')
    phone = PhoneNumberField(blank=True, default='')    
    homepage = models.URLField(blank=True, default='')
    visible = models.BooleanField(default=True)
    template = models.CharField(max_length=128, default='2015-artist.html')
    css = models.TextField(blank=True, default='')
    javascript = models.TextField(blank=True, default='')
    
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
    
 




    
        
class Art(models.Model):
    artist = models.ForeignKey(Artist)
    title = models.CharField(max_length=128, blank=True, default='')
    slug = models.SlugField(max_length=128)
    description = models.TextField(blank=True, default='')

    def __unicode__(self):
        return "{} {}".format(self.artist_name(), self.title)
    
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
        