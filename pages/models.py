from django.db import models
import os
from uuid import uuid4
from django.utils.text import slugify

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit

def path_and_rename(instance, filename):
    document_path(instance, filename, 'poster', 'images')
    
    
def poster_path(instance, filename):
    ext = filename.split('.')[-1]
    # get filename
    slug = slugify(instance.title+'-'+instance.dir_by)
    filename = 'mykonos-biennale-2015-film-festival-{}-{}.{}'.format(slug,'poster', ext)
    return os.path.join('images', filename)

def image_path(instance, filename):
    ext = filename.split('.')[-1]
    # get filename
    slug = slugify(instance.film.title+'-'+instance.title+'-'+instance.film.dir_by)
    count = instance.film.filmfestival_image_related.count()
    filename = 'mykonos-biennale-2015-film-festival-{}-{}-{}.{}'.format(slug, instance.image_type, count,  ext)
    return os.path.join('images', filename)
    
def headshot_path(instance, filename):
     document_path(instance, filename, 'headshot', 'images')
        
def screenshot_path(instance, filename):
     document_path(instance, filename, 'screenshot', 'images')

def still_path(instance, filename):
    document_path(instance, filename, 'still', 'images')

def document_path(instance, filename, prefix='document',path='documents'):
    ext = filename.split('.')[-1]
    slug = slugify(instance.film.title+'-'+instance.film.dir_by)
    filename = 'mykonos-biennale-2015-film-festival-{}-{}.{}'.format(slug, prefix, instance.id, ext)
    return os.path.join(path, filename)

class Page(models.Model):
    class Meta:
        ordering = ['order']
    festival = models.CharField(max_length=200)
    order = models.IntegerField()
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    template = models.CharField(max_length=128, default='page.html')
    description_155 =    models.TextField( blank=True, default='')
    description_200 =    models.TextField( blank=True, default='')
    description_300 =    models.TextField( blank=True, default='')
    image  = models.ImageField (upload_to=poster_path,  max_length=256, blank=True)
    image_to_use = ImageSpecField(source='image',
                                      processors=[ResizeToFit(280,280)],
                                      format='JPEG',
                                      options={'quality': 60})
    url = models.URLField(blank=True, default='')
    visible = models.BooleanField(default=True)
    css = models.TextField(default='')
    javascript = models.TextField(default='')
    def __unicode__(self):
        return self.title
    
    def panels(self):
        return self.panel_set.filter(visible=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)
    
    
class Panel(models.Model):
    class Meta:
        ordering = ['order']
    page = models.ForeignKey(Page)
    order = models.IntegerField()
    title = models.CharField(max_length=128, blank=True, default='')
    slug = models.SlugField(max_length=200)
    content = models.TextField(blank=True, default='')
    css = models.TextField(default='')
    visible = models.BooleanField(default=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Panel, self).save(*args, **kwargs)