# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import festivalA.models


class Migration(migrations.Migration):

    dependencies = [
        ('festivalA', '0005_auto_20151021_0453'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='photo',
            field=models.ImageField(max_length=256, upload_to=festivalA.models.art_image_path, blank=True),
        ),
    ]
