# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festival', '0009_art_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='leader',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='art',
            name='show',
            field=models.BooleanField(default=True),
        ),
    ]
