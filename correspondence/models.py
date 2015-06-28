# from django.db import models

# # Create your models here.
# from filmfestival.models import Film
# from festival.models import Artist
# class Posting(models.Model):
#     subject = models.CharField(max_length=128)
    
# class Mail(models.Model):
#     subject = models.CharField(max_length=128)
#     recipient = models.EmailField(blank=True, default='')
#     film = models.TextField(Film,blank=True, default=None)
    
#     artist = models.TextField(Film,blank=True, default=None)
#     name = models.CharField(max_length=128)
#     message = models.TextField()
    
#     country = CountryField(blank=True, default='')
#     phone = PhoneNumberField(blank=True, default='')
#     headshot  = models.ImageField (upload_to=headshot_path,  max_length=256, blank=True)