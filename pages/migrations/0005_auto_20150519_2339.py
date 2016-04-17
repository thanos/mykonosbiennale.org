# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20150519_2109'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='panel',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='panel',
            name='order',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
