# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_auto_20160704_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='css',
            field=models.TextField(default=b'', blank=True),
        ),
    ]
