# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmfestival', '0016_auto_20150610_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screening',
            name='time',
            field=models.TimeField(default=None, null=True),
        ),
    ]
