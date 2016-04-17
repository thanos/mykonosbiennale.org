# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('filmfestival', '0011_auto_20150610_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='day',
            name='runtime',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='screening',
            name='time',
            field=models.TimeField(default=datetime.datetime(2015, 6, 10, 14, 54, 35, 375260)),
            preserve_default=False,
        ),
    ]
