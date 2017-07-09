# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_auto_20160704_0603'),
    ]

    operations = [
        migrations.AddField(
            model_name='slideshow',
            name='content',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AddField(
            model_name='slideshow',
            name='css',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AddField(
            model_name='slideshow',
            name='static_content',
            field=models.BooleanField(default=False),
        ),
    ]
