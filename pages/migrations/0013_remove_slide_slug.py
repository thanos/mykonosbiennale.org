# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_slide'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slide',
            name='slug',
        ),
    ]
