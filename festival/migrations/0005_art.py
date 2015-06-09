# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import festival.models


class Migration(migrations.Migration):

    dependencies = [
        ('festival', '0004_auto_20150608_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=128, blank=True)),
                ('slug', models.SlugField(max_length=128)),
                ('description', models.TextField(default=b'', blank=True)),
                ('text', models.TextField(default=b'', blank=True)),
                ('photo', models.ImageField(max_length=256, upload_to=festival.models.artNamer, blank=True)),
                ('artist', models.ForeignKey(to='festival.Artist')),
            ],
        ),
    ]
