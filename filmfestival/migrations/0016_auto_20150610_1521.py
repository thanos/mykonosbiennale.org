# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmfestival', '0015_auto_20150610_1511'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='screening',
            options={'ordering': ('time',), 'get_latest_by': 'time'},
        ),
        migrations.RenameField(
            model_name='day',
            old_name='time',
            new_name='start_time',
        ),
    ]
