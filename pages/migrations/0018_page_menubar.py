# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_slideshow_delay'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='menubar',
            field=models.BooleanField(default=True),
        ),
    ]
