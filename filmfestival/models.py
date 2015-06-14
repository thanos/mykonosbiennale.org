from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
import os,datetime
from uuid import uuid4
from django.utils.text import slugify

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit
from sorl.thumbnail import ImageField
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


class Program(models.Model):
    slug = models.SlugField(max_length=200)
    title = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title+'-program')
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
        return 0
    
    def __unicode__(self):
        return "{} {}".format(self.program, self.date)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(str(self))
        super(Day, self).save(*args, **kwargs)
        
        
class Screening(models.Model):
    class Meta:
        ordering  = ('start_time',)
        get_latest_by ="start_time"
        
    day = models.ForeignKey(Day)
    pause = models.IntegerField(default=3)
    film = models.ForeignKey('Film')  
    slug = models.SlugField(max_length=200)
    start_time = models.DateTimeField(blank=True, default=None)
    
    def __unicode__(self):
        return "{} {} {}".format(self.day.program, self.start_time, self.film.title)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(str(self))
        if self.id is None:
            try:
                last = Screening.objects.filter(day=self.day).latest()
                self.start_time =  last.start_time
                self.start_time  += datetime.timedelta(minutes=last.film.runtime)
            except Screening.DoesNotExist:
                self.start_time = datetime.datetime.combine(self.day.date, self.day.start_time)
            self.start_time  += datetime.timedelta(minutes=self.pause)
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
    original_title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    dir_by = models.CharField(max_length=128)
    sub_by = models.CharField(max_length=128, default='')
    subtitles = models.BooleanField(default=False)
    language= models.CharField(max_length=128)
    actors = models.TextField()
    year = models.CharField(max_length=4)
    runtime = models.IntegerField()
    country = models.TextField()
    #coming = models.BooleanField(default= False)


    log_line = models.TextField(default='')
    synopsis = models.TextField(default='')
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
    trailer = models.URLField(blank=True, default='')
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
    def __unicode__(self):
        return self.title
    

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
    image_thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFit(1000, 150)],
                                      format='JPEG',
                                      options={'quality': 60})
    image_for_download = ImageSpecField(source='image',
                                      processors=[ResizeToFit(1000,1000)],
                                      format='JPEG',
                                      options={'quality': 90})
    
class Documentation(Material):
    file = models.FileField(upload_to=document_path, max_length=256, blank=True)
