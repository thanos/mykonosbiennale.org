# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('festival', '0011_remove_artist_festival'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectSeason',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('festival', models.ForeignKey(to='festival.Festival')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectX',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(populate_from=b'title', editable=False)),
                ('festival', models.ManyToManyField(to='festival.Festival', through='festival.ProjectSeason')),
            ],
        ),
        migrations.AddField(
            model_name='projectseason',
            name='project',
            field=models.ForeignKey(to='festival.ProjectX'),
        ),
    ]
