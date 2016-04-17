# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filmfestival.models


class Migration(migrations.Migration):

    dependencies = [
        ('filmfestival', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('slug', models.SlugField(max_length=200)),
                ('info', models.TextField(default=b'')),
                ('image_type', models.CharField(default=b'Screenshot', max_length=10, choices=[(b'Still', b'Still'), (b'Screenshot', b'Screenshot')])),
                ('image', models.ImageField(max_length=256, upload_to=filmfestival.models.screenshot_path, blank=True)),
                ('film', models.ForeignKey(related_name='filmfestival_image_related', to='filmfestival.Film')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='screenshot',
            name='film',
        ),
        migrations.RemoveField(
            model_name='still',
            name='film',
        ),
        migrations.DeleteModel(
            name='Screenshot',
        ),
        migrations.DeleteModel(
            name='Still',
        ),
    ]
