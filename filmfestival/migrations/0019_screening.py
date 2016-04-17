# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmfestival', '0018_auto_20150610_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Screening',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pause', models.IntegerField(default=3)),
                ('slug', models.SlugField(max_length=200)),
                ('start_time', models.DateTimeField(default=None, blank=True)),
                ('day', models.ForeignKey(to='filmfestival.Day')),
                ('film', models.ForeignKey(to='filmfestival.Film')),
            ],
            options={
                'ordering': ('start_time',),
                'get_latest_by': 'start_time',
            },
        ),
    ]
