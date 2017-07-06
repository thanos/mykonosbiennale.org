# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('festivaly', '0004_auto_20170523_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='facebook',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='instagram',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='twitter',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
    ]
