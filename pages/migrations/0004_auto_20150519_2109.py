# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150519_1827'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='templates',
            new_name='template',
        ),
    ]
