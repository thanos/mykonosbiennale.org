# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmfestival', '0005_auto_20150519_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='facebook',
            field=models.CharField(default=b'', max_length=164, blank=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='first_time',
            field=models.CharField(default=b'', max_length=164, blank=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='other_social_media',
            field=models.CharField(default=b'', max_length=164, blank=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='status',
            field=models.CharField(default=b'', max_length=164, blank=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='twitter',
            field=models.CharField(default=b'', max_length=164, blank=True),
        ),
    ]
