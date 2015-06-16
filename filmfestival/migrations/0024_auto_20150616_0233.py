# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmfestival', '0023_auto_20150615_2108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='notes',
        ),
        migrations.AddField(
            model_name='film',
            name='when',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
    ]
