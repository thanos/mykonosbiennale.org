# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessedImage',
            fields=[
                ('source_image', models.URLField(max_length=1024, serialize=False, primary_key=True)),
                ('processed_image', models.URLField(max_length=1024)),
            ],
        ),
    ]
