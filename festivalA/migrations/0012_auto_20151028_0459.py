# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields
import festivalA.models


class Migration(migrations.Migration):

    dependencies = [
        ('festivalA', '0011_auto_20151028_0424'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='festival',
            name='year',
            field=models.IntegerField(default=2015),
        ),
        migrations.AddField(
            model_name='project',
            name='festival',
            field=models.ForeignKey(default=None, to='festivalA.Festival'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='location',
            name='image',
            field=sorl.thumbnail.fields.ImageField(default=None, max_length=256, upload_to=festivalA.models.location_image_path, blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(to='festivalA.Location'),
        ),
        migrations.AddField(
            model_name='event',
            name='project',
            field=models.ForeignKey(to='festivalA.Project'),
        ),
        migrations.AddField(
            model_name='art',
            name='events',
            field=models.ManyToManyField(related_name='art_exhibited', to='festivalA.Event'),
        ),
    ]
