# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filmfestival.models


class Migration(migrations.Migration):

    dependencies = [
        ('filmfestival', '0003_auto_20150504_0301'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='trailer',
            field=models.URLField(default=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='documentation',
            name='info',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(max_length=256, upload_to=filmfestival.models.image_path, blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='info',
            field=models.TextField(default=b'', blank=True),
        ),
    ]
