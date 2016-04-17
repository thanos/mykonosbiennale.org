# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmfestival', '0013_auto_20150610_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day',
            name='program',
        ),
        migrations.RemoveField(
            model_name='screening',
            name='day',
        ),
        migrations.RemoveField(
            model_name='screening',
            name='film',
        ),
        migrations.DeleteModel(
            name='Day',
        ),
        migrations.DeleteModel(
            name='Program',
        ),
        migrations.DeleteModel(
            name='Screening',
        ),
    ]
