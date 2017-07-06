# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('festival', '0010_auto_20170320_0308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='festival',
        ),
    ]
