# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmfestival', '0007_auto_20150524_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='coming',
            field=models.BooleanField(default=False),
        ),
    ]
