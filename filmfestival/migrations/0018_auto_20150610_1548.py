# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmfestival', '0017_auto_20150610_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='screening',
            name='day',
        ),
        migrations.RemoveField(
            model_name='screening',
            name='film',
        ),
        migrations.DeleteModel(
            name='Screening',
        ),
    ]
