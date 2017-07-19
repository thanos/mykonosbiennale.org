# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('festival', '0014_auto_20170517_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='last_festival',
            field=models.IntegerField(default=2015),
        ),
    ]
