from django.db import models
from django_countries.fields import CountryField
from django.utils.text import slugify
from django.core.urlresolvers import reverse

from phonenumber_field.modelfields import PhoneNumberField
import os,datetime
from uuid import uuid4
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit
from sorl.thumbnail import ImageField

from material.models  import Album

def path_and_rename(instance, filename):
    document_path(instance, filename, 'poster', 'images')
    
    
def poster_path(instance, filename):
    base, ext = os.path.splitext(filename)
    # get filename
    slug = slugify(instance.title+'-'+instance.dir_by)
    filename = 'mykonos-biennale-2015-film-festival-{}-{}{}'.format(slug,'poster', ext)
    return os.path.join('images', filename)

def location_image_path(instance, filename):
    base, ext = os.path.splitext(filename)
    # get filename
    slug = slugify(instance.name)
    filename = 'mykonos-biennale-2015-{}-{}{}'.format('location', slug, ext)
    return os.path.join('images', filename)

def image_path(instance, filename):
    base, ext = os.path.splitext(filename)
    # get filename
    slug = slugify(instance.film.title+'-'+instance.title+'-'+instance.film.dir_by)
    count = instance.film.filmfestival_image_related.count()
    filename = 'mykonos-biennale-2015-film-festival-{}-{}-{}{}'.format(slug, instance.image_type, count,  ext)
    return os.path.join('images', filename)
    
def headshot_path(instance, filename):
     document_path(instance, filename, 'headshot', 'images')
        
def screenshot_path(instance, filename):
     document_path(instance, filename, 'screenshot', 'images')

def still_path(instance, filename):
    document_path(instance, filename, 'still', 'images')

def document_path(instance, filename, prefix='document',path='documents'):
    base, ext = os.path.splitext(filename)
    slug = slugify(instance.film.title+'-'+instance.film.dir_by)
    filename = 'mykonos-biennale-2015-film-festival-{}-{}{}'.format(slug, prefix, instance.id, ext)
    return os.path.join(path, filename)

class Award(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image  = ImageField (upload_to=image_path,  max_length=256, blank=True)
    description  = models.TextField()

    def __unicode__(self):
        return "{} {}".format(self.name, self.description)
	
        
class Reward(models.Model):
    film = models.ForeignKey('Film') 
    award = models.ForeignKey('Award') 
    description  = models.TextField()

    def __unicode__(self):
        return "{} {}".format(self.film.title, self.award)
	


class Location(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image  = ImageField (upload_to=location_image_path,  max_length=256, blank=True)
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
    
class Program(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('program', args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Program, self).save(*args, **kwargs)

class Day(models.Model):
    class Meta:
        ordering = ['date']
    program = models.ForeignKey(Program)
    date = models.DateField()
    slug = models.SlugField(max_length=200)
    runtime = models.IntegerField(default=0)
    start_time = models.TimeField(default="21:00")
    
    def number_of_films(self):
        return self.screening_set.count()
    
    def __unicode__(self):
        return "{} {}".format(self.program, self.date)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(str(self))
        super(Day, self).save(*args, **kwargs)
        
    def build_timetable(self):
        previous_screening = None
        runtime = 0
        count =  10
        for screening in self.screening_set.all():
            runtime += screening.film.runtime
            screening.schedule(previous_screening)
            screening.save()
            previous_screening = screening
            print "%02d-%03d-%s %s" % ( self.date.day, count, slugify(screening.film.title), screening.film.projection_copy_url)
            count +=10
        self.runtime = runtime
        self.save()
            
    def first_screening(self):
        try:
            return self.screening_set.first()
        except Screening.DoesNotExist:
            pass
        
    def last_screening(self):
        try:
            return self.screening_set.last()
        except Screening.DoesNotExist:
            pass
                
class Screening(models.Model):
    class Meta:
        ordering  = ('id',)
        get_latest_by ="start_time"
        
    day = models.ForeignKey(Day, blank=True, null=None)
    pause = models.IntegerField(default=3)
    film = models.ForeignKey('Film') 
    location = models.ForeignKey('Location', blank=True, null=True) 
    slug = models.SlugField(max_length=200)
    start_time = models.DateTimeField(blank=True, default=None)
    
    def __unicode__(self):
        return "{} {} {}".format(self.day.program, self.start_time, self.film.title)
    
    def schedule(self, previous_screening=None):
        if previous_screening:
            self.start_time =  previous_screening.start_time
            self.start_time  += datetime.timedelta(minutes=previous_screening.film.runtime+previous_screening.pause)
        else:
            self.start_time = datetime.datetime.combine(self.day.date, self.day.start_time)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(str(self))
        if self.id is None:
            self.schedule(self.day.last_screening())
        super(Screening, self).save(*args, **kwargs)
    
    
class Film(models.Model):
    class Meta:
        ordering = ['ref']
    DRAMATIC_NIGHTS = 'Dramatic Nights'
    VIDEO_GRAFITTI = 'Video Grafitti'
    DANCE = 'Dance'
    DOCUMENTARY = 'Documentary'
    FILM_TYPES_CHOICES = (
        (DRAMATIC_NIGHTS, 'Dramatic Nights'),
        (VIDEO_GRAFITTI, 'Video Graffiti'),
        (DANCE, 'Dance'),
        (DOCUMENTARY, 'Documentary'),
    )
    SELECTED = 'SELECTED'
    UNDECIDED = 'UNDECIDED'
    OUT = 'OUT'
    ENTRY_STATUS_CHOICES = (
     (SELECTED, 'Selected'),
        (UNDECIDED, 'Undecided'),
        (OUT, 'Out'),
    )
    WITHOUTABOX = 'WITHOUTABOX'
    FILMFREEWAY = 'UNDECIDED'
    OTHER = 'OUT'
    FILM_SOURCE_CHOICES = (
     (WITHOUTABOX, 'Withoutabox'),
        (FILMFREEWAY, 'Filmfreeway'),
        (OTHER, 'Other'),
    )

    ref = models.CharField(max_length=30)
    source = models.CharField(max_length=30,
                                      choices=FILM_SOURCE_CHOICES,
                                      default=WITHOUTABOX)
    
    title = models.CharField(max_length=200)
    original_title = models.CharField(max_length=200,blank=True, default='')
    slug = models.SlugField(max_length=200)
    dir_by = models.CharField(max_length=128)
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
    #coming = models.BooleanField(default= False)
    projection_copy = models.BooleanField(default= False)
    projection_copy_url = models.URLField(blank=True, default='')
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
    directors = models.TextField(blank=True, default='')
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
    status = models.CharField(max_length=164,   choices=ENTRY_STATUS_CHOICES, default = UNDECIDED)
    url = models.URLField(blank=True, default='')
    
    trailer_url = models.URLField(blank=True, default='')
    trailer_embed = models.TextField(blank=True, default='')
    genres = models.CharField(max_length=128, blank=True, default='')
    niches = models.CharField(max_length=256, blank=True, default='')
    info = models.TextField(blank=True, default='')
    directors_statement = models.TextField(blank=True, default='')
    production_notes = models.TextField(blank=True, default='')
    film_type = models.CharField(max_length=30,
                                      choices=FILM_TYPES_CHOICES,
                                      default=DRAMATIC_NIGHTS)
    
    crew = models.TextField(blank=True, default='')
    
    poster  = ImageField (upload_to=poster_path,  max_length=256, blank=True)
    poster_thumbnail = ImageSpecField(source='poster',
                                      processors=[ResizeToFit(150,300)],
                                      format='JPEG',
                                      options={'quality': 60})
    poster_for_download = ImageSpecField(source='poster',
                                      processors=[ResizeToFit(1000,1000)],
                                      format='JPEG',
                                      options={'quality': 90})
    stills = models.ForeignKey(Album,  blank=True, null=True) 
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('film-detail', args=[self.slug])
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title+'-'+self.dir_by)
        super(Film, self).save(*args, **kwargs)
    
class Person(models.Model):
    film = models.ForeignKey(Film)
    name = models.CharField(max_length=128)
    what = models.CharField(max_length=128)
    email = models.EmailField(blank=True, default='')
    country = CountryField(blank=True, default='')
    phone = PhoneNumberField(blank=True, default='')
    headshot  = models.ImageField (upload_to=headshot_path,  max_length=256, blank=True)
    
class Material(models.Model):
    film = models.ForeignKey(Film, related_name="%(app_label)s_%(class)s_related")
    title = models.CharField(max_length=128, blank=True, default='')
    slug = models.SlugField(max_length=200)
    info = models.TextField(blank=True, default='')
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = self.film.title
        self.slug = slugify(self.title)
        super(Material, self).save(*args, **kwargs)
        


	


class Image(Material):
    STILL = 'Still'
    SCREENSHOT = 'Screenshot'
    IMAGE_TYPES_CHOICES = (
        (STILL, STILL),
        (SCREENSHOT, SCREENSHOT),
    )
    image_type = models.CharField(max_length=len(SCREENSHOT),
                                      choices=IMAGE_TYPES_CHOICES,
                                      default=SCREENSHOT)
    image = models.ImageField (upload_to=image_path,  max_length=256, blank=True)

    
class Documentation(Material):
    file = models.FileField(upload_to=document_path, max_length=256, blank=True)
