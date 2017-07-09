# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('festivaly', '0005_auto_20170523_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='homepage',
            field=models.URLField(default=b'', blank=True),
        ),
    ]
