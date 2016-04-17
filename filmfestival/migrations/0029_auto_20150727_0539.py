# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import filmfestival.models


class Migration(migrations.Migration):

    dependencies = [
        ('filmfestival', '0028_auto_20150622_0051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('image', sorl.thumbnail.fields.ImageField(max_length=256, upload_to=filmfestival.models.image_path, blank=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='screening',
            options={'ordering': ('id',), 'get_latest_by': 'start_time'},
        ),
    ]
