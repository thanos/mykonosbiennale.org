# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('festival', '0013_art_project_x'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='festival',
            options={'ordering': ['year', 'title']},
        ),
        migrations.AddField(
            model_name='festival',
            name='year',
            field=models.IntegerField(default=2015),
        ),
        migrations.AddField(
            model_name='projectx',
            name='statement',
            field=models.TextField(default=b''),
        ),
    ]
