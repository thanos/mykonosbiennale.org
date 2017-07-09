from django.db import models
import os
from uuid import uuid4
from django.utils.text import slugify
from django.core.urlresolvers import reverse

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit

def path_and_rename(instance, filename):
    document_path(instance, filename, 'poster', 'images')
    
    
def slide_show_image(instance, filename):
    ext = filename.split('.')[-1]
    # get filename
    if instance.title:
      filename = 'mykonos biennale 2015 art festival antidote {} {} {}'.format(instance.slide_show.title, instance.title, instance.pk)
    else:
      filename = 'mykonos biennale 2015 festival antidote {} {}'.format(instance.slide_show.title, instance.pk)
    slug = slugify(filename)+'.'+ext
    return os.path.join('images', 'slides',slug)    
    
    
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
    in_menubar = models.BooleanField(default=True)
    css = models.TextField(default='')
    javascript = models.TextField(default='')

    @classmethod
    def menubar(cls):
        return cls.objects.filter(in_menubar=True, visible=True)
    
    def panels(self):
        return self.panel_set.filter(visible=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)

    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('page', args=[self.slug])        
        

    
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
    slide_show  = models.ForeignKey('SlideShow', blank=True, null=True)
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Panel, self).save(*args, **kwargs)
        
        
    def get_absolute_url(self):
        return "{}#{}".format(self.page.get_absolute_url(), self.slug)
    
from imagekit import ImageSpec, register
from imagekit.processors import ResizeToFill

class SlideImage(ImageSpec):
    processors = [ResizeToFill(800, 700)]
    format = 'JPEG'
    options = {'quality': 60}

register.generator('mb:slideimage', SlideImage)
    
class SlideShow(models.Model):
    class Meta:
        ordering = ['title']
    title = models.CharField(max_length=128, blank=True, default='')
    slug = models.SlugField(max_length=200)
    content = models.TextField(blank=True, default='')
    css = models.TextField(blank=True, default='')
    static_content = models.BooleanField(default=False)
    delay = models.IntegerField(default=3)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(SlideShow, self).save(*args, **kwargs)
        
    def __unicode__(self):
        return self.title   
    
    def visible_slides(self):
        return self.slide_set.filter(visible=True)
    
    
    
class Slide(models.Model):
    class Meta:
        ordering = ['order']
    slide_show  = models.ForeignKey(SlideShow)
    order = models.IntegerField()
    title = models.CharField(max_length=128, blank=True, default='')
    #slug = models.SlugField(max_length=200)    
    content = models.TextField(blank=True, default='')
    css = models.TextField(blank=True, default='')
    visible = models.BooleanField(default=True)
    image  = models.ImageField (upload_to=slide_show_image,  blank=True)
    
#     image_to_use = ImageSpecField(source='image',
#                                       processors=[ResizeToFit(1300,750)],
#                                       format='JPEG',
#                                       options={'quality': 60})
    video  = models.FileField (upload_to=slide_show_image,  max_length=256, blank=True)
    
    
    def image_tag(self):
      return u'<img height="175" src="%s" />' % self.image.url if self.image else ''
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
    
    
    def save(self, *args, **kwargs):
        #if not self.slug:
        #  self.slug = "{} slide {}".format(self.slide_show.title, self.slide_show.slide_set.count())
        #print "SLUG", self.slug
        #self.slug = slugify(self.slug)
        super(Slide, self).save(*args, **kwargs)

        
    def __unicode__(self):
        return self.title  if self.title else 'order-{}'.format(self.order)  

    

