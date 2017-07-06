# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('festivaly', '0002_auto_20170523_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='headshot',
            field=versatileimagefield.fields.VersatileImageField(upload_to=b'material/', null=True, verbose_name=b'image', blank=True),
        ),
    ]
