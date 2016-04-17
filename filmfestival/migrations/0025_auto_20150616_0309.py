# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmfestival', '0024_auto_20150616_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='when',
            field=models.CharField(default=b'', max_length=64, blank=True),
        ),
    ]
