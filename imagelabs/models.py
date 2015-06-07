from django.db import models
from django.utils.text import slugify



class ProcessedImage(models.Model):
    source_image = models.URLField(max_length=1024, primary_key=True)
    processed_image = models.URLField(max_length=1024) 
    def __unicode__(self):
        return self.processed_image