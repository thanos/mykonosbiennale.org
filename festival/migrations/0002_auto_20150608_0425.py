# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('festival', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='css',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='javascript',
            field=models.TextField(default=b'', blank=True),
        ),
    ]
