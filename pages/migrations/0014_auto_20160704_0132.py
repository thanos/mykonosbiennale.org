# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import pages.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_remove_slide_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='video',
            field=models.FileField(max_length=256, upload_to=pages.models.slide_show_image, blank=True),
        ),
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=models.ImageField(upload_to=pages.models.slide_show_image, blank=True),
        ),
    ]
