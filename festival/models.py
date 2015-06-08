from django.db import models
import os
from uuid import uuid4
from django.utils.text import slugify
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit


class ImageNamer:
    folder = 'artists'
    postfix = ''
    def __call__(self, instance, filename):
        store_filename = self.image_path(instance, filename)
        return os.path.join(self.folder, store_filename)
    def image_path(self, instance, filename):
        return 'mykonos-biennale-'+slugify(self.image_name(instance, filename))

    
class ArtNamer(ImageNamer):
    def image_name(self, instance, filename):
        ext = filename.split('.')[-1]
        artist = instance.artist
        count = 0
        return "{}-{}-{}-{}.{}".format(
                artist.festival, 
                artist.name, 
                instance.title, 
                count, ext)

def artNamer(instance, filename):
    return ArtNamer()(instance, filename)
    
class PosterNamer(ImageNamer):
    def image_name(self, instance, filename):
        ext = filename.split('.')[-1]
        return "{}-{}-poster.{}".format(
                instance.festival, 
                instance.name,
                ext)

def posterNamer(instance, filename):
    return PosterNamer()(instance, filename)
    
class HeadshotNamer(ImageNamer):
    def image_name(self, instance, filename):
        ext = filename.split('.')[-1]
        return "{}-{}-headshot.{}".format(
                instance.festival, 
                instance.name,
                ext)

def headshotNamer(instance, filename):
    return HeadshotNamer()(instance, filename)


class Festival(models.Model):
    class Meta:
        ordering = ['title']
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    statement = models.TextField(default='')
    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Festival, self).save(*args, **kwargs)
        

        

class Artist(models.Model):
    class Meta:
        ordering = ['name']
    TEASURE_HUNT = 'TEASURE HUNT'
    OTHER = 'OTHER'
    KITE_FESTIVAL = 'KITE FESTIVAL'
    EVENT_CHOICES = (
     (TEASURE_HUNT, TEASURE_HUNT),
        
        (KITE_FESTIVAL, KITE_FESTIVAL),
        (OTHER, OTHER),
    )


    festival = models.ForeignKey(Festival)
    event = models.CharField(max_length=64,
                                      choices=EVENT_CHOICES,
                                      default=TEASURE_HUNT)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    template = models.CharField(max_length=128, default='2015-artist.html')
    bio =    models.TextField( blank=True, default='')
    statement =    models.TextField( blank=True, default='')
    email = models.EmailField(blank=True, default='')
    country = CountryField(blank=True, default='')
    phone = PhoneNumberField(blank=True, default='')    
    headshot  = models.ImageField (upload_to=headshotNamer, max_length=256, blank=True)
    headshot_to_use = ImageSpecField(source='headshot',
                                      processors=[ResizeToFit(150,150)],
                                      format='JPEG',
                                      options={'quality': 60})
    homepage = models.URLField(blank=True, default='')
    poster  = models.ImageField (upload_to=posterNamer,  max_length=256, blank=True)
    poster_thumbnail = ImageSpecField(source='poster',
                                      processors=[ResizeToFit(150,300)],
                                      format='JPEG',
                                      options={'quality': 60})
    visible = models.BooleanField(default=True)
    css = models.TextField(blank=True, default='')
    javascript = models.TextField(blank=True, default='')
    
    def __unicode__(self):
        return self.name
    
    def artists(self):
        return self.panel_set.filter(visible=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Artist, self).save(*args, **kwargs)
        
class Art(models.Model):
    artist = models.ForeignKey(Artist)
    title = models.CharField(max_length=128, blank=True, default='')
    slug = models.SlugField(max_length=128)
    description = models.TextField(blank=True, default='')
    text = models.TextField(blank=True, default='')
    image = models.ImageField (upload_to=artNamer, max_length=256, blank=True)
    image_thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFit(1000, 150)],
                                      format='JPEG',
                                      options={'quality': 60})
    image_for_download = ImageSpecField(source='image',
                                      processors=[ResizeToFit(1000,1000)],
                                      format='JPEG',
                                      options={'quality': 90})

    def __unicode__(self):
        return "{} {}".format(self.artist, self.title)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Art, self).save(*args, **kwargs)