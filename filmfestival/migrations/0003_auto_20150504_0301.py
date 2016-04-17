# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmfestival', '0002_auto_20150504_0252'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='crew',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='art_directors',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='cinematographers',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='co_producers',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='composers',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='directors',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='editors',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='exec_producers',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='producers',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='product_designers',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='screenings',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='screenwriters',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='sound_editors',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='synopsis_125',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='synopsis_250',
            field=models.TextField(default=b'', blank=True),
        ),
    ]
