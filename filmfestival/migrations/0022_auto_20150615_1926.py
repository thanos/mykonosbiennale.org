# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmfestival', '0021_auto_20150615_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='notes',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='film',
            name='present',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='film',
            name='projection_copy',
            field=models.BooleanField(default=False),
        ),
    ]
