# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0002_auto_20170327_0215'),
        ('filmfestival', '0030_reward'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='stills',
            field=models.ForeignKey(blank=True, to='material.Album', null=True),
        ),
    ]
