# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import filmfestival.models


class Migration(migrations.Migration):

    dependencies = [
        ('filmfestival', '0008_film_coming'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='poster',
            field=sorl.thumbnail.fields.ImageField(max_length=256, upload_to=filmfestival.models.poster_path, blank=True),
        ),
    ]
