# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import pages.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_slide_slideshow'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='slide_show',
            field=models.ForeignKey(default=1, to='pages.SlideShow'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=models.ImageField(max_length=256, upload_to=pages.models.slide_show_image, blank=True),
        ),
    ]
