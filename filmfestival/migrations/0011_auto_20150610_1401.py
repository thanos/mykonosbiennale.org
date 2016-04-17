# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmfestival', '0010_auto_20150610_1341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='coming',
        ),
        migrations.AddField(
            model_name='day',
            name='slug',
            field=models.SlugField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='program',
            name='slug',
            field=models.SlugField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='screening',
            name='pause',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='screening',
            name='slug',
            field=models.SlugField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='screening',
            name='day',
            field=models.ForeignKey(to='filmfestival.Day'),
        ),
    ]
