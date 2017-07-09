from django.db import models

import tagulous.models

from photologue.models import Gallery


class Album(models.Model):
    selection = models.OneToOneField(Gallery, related_name='extended')
    tags = tagulous.models.TagField(default='')
    def __str__(self):
        return self.photos.title