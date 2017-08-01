import collections
import os

from autoslug import AutoSlugField
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify
from django_countries.fields import CountryField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from phonenumber_field.modelfields import PhoneNumberField


class ImageNamer:
    folder = 'artists'
    postfix = ''
    def __call__(self, instance, filename):
        base, ext = os.path.splitext(filename)
        store_filename = 'mykonos-biennale-{}{}'.format(slugify(self.image_name(instance, base)),ext)
        return os.path.join(self.folder, store_filename)

    
class ArtNamer(ImageNamer):
    def image_name(self, instance, filename):
        artist = instance.artist
        count = instance.artist.art_set.count()
        return "{}-{}-{}-{}".format(
            instance.project_x,
                artist.name, 
                instance.title, count)

def artNamer(instance, filename):
    return ArtNamer()(instance, filename)
    
class PosterNamer(ImageNamer):
    def image_name(self, instance, filename):
        return "{}-{}-poster".format(
                instance.festival, 
                instance.name)

def posterNamer(instance, filename):
    return PosterNamer()(instance, filename)
    
class HeadshotNamer(ImageNamer):
    def image_name(self, instance, filename):
        return "mykonos-biennale-artist-{}".format(
                instance.name)

def headshotNamer(instance, filename):
    return HeadshotNamer()(instance, filename)


class Festival(models.Model):
    class Meta:
        ordering = ['year', 'title']
    year = models.IntegerField(default= 2015)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    statement = models.TextField(default='')

    @property
    def label(self):
        return '{}-{}'.format(self.year, self.title)

    def __unicode__(self):
        return self.label

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Festival, self).save(*args, **kwargs)


class ProjectSeason(models.Model):
	festival = models.ForeignKey('Festival')
	project = models.ForeignKey('ProjectX')
	def __unicode__(self):
		return "{} {}".format(self.festival.year, self.project.title)

	
class ProjectX(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    festival = models.ManyToManyField(Festival, through='ProjectSeason')
    statement = models.TextField(default='')


    @property
    def label(self):
        return '{}-{}'.format(self.festival.label, self.title)

    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('project', args=[self.slug])
	
	
class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    festival = models.ForeignKey('Festival')
    def __unicode__(self):
        return "{} {}".format(self.festival.year, self.title)
    
    def get_absolute_url(self):
        return reverse('project', args=[self.slug])
    

	


class Artist(models.Model):
    class Meta:
        ordering = ['name']
    TEASURE_HUNT = 'TREASURE HUNT'
    OTHER = 'OTHER'
    KITE_FESTIVAL = 'KITE FESTIVAL'
    PROJECT_X = 'PROJECT X'
    INTERGRATIONS  = 'INTERGRATIONS'
    ARCHEOLOGICAL_MUSEUM  = 'ARCHEOLOGICAL MUSEUM'
    PDF_JPEG  = 'PDF-JPEG'
    EVENT_CHOICES = (
		(ARCHEOLOGICAL_MUSEUM, ARCHEOLOGICAL_MUSEUM),
        (TEASURE_HUNT, TEASURE_HUNT),
        (KITE_FESTIVAL, KITE_FESTIVAL),
        (PROJECT_X, PROJECT_X),
		(INTERGRATIONS, INTERGRATIONS),
		(PDF_JPEG, PDF_JPEG),
        (OTHER, OTHER),
    )


    last_festival = models.IntegerField(default= 2015)
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
    
    def get_absolute_url(self):
        return reverse('artist-detail', args=[self.slug]) 
    
    def artists(self):
        return self.panel_set.filter(visible=True)

    def art_by_project(self):
        projects = collections.defaultdict(list)
        for art in self.art_set.filter(show=True):
          projects[art.project_x].append(art)
        return [ {'project': project, 'art':projects[project]} for project in sorted(projects, key=lambda x:x.project.title)]

    def artwork(self):
        try:
            return self.art_set.first().photo.url
        except: 
            pass 
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Artist, self).save(*args, **kwargs)
        
class Art(models.Model):
    artist = models.ForeignKey(Artist)
    project = models.ForeignKey(Project)
    project_x = models.ForeignKey(ProjectSeason,  blank=True, null=True)
    title = models.CharField(max_length=128, blank=True, default='')
    slug = models.SlugField(max_length=128)
    show = models.BooleanField(default=True)
    leader = models.BooleanField(default=True)
    description = models.TextField(blank=True, default='')
    text = models.TextField(blank=True, default='')
    photo = models.ImageField (upload_to=artNamer, max_length=256, blank=True)

    def image_tag(self):
      return u'<img height="75" src="%s" />' % self.photo.url
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


  
    #project = models.ForeignKey('Project')

    def __unicode__(self):
        return "{} {}".format(self.artist, self.title)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Art, self).save(*args, **kwargs)
