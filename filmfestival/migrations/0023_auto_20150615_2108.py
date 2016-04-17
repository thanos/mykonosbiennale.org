# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmfestival', '0022_auto_20150615_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='projection_copy_url',
            field=models.URLField(default=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='actors',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='country',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='language',
            field=models.CharField(default=b'', max_length=128, blank=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='log_line',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='original_title',
            field=models.CharField(default=b'', max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='synopsis',
            field=models.TextField(default=b'', blank=True),
        ),
    ]
