# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='gallery',
            new_name='selection',
        ),
    ]
