# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_auto_20170329_0435'),
    ]

    operations = [
        migrations.AddField(
            model_name='slideshow',
            name='delay',
            field=models.IntegerField(default=3),
        ),
    ]
