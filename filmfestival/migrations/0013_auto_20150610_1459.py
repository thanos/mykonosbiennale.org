# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmfestival', '0012_auto_20150610_1454'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='screening',
            options={'ordering': ('order',)},
        ),
        migrations.AddField(
            model_name='screening',
            name='order',
            field=models.PositiveIntegerField(default=1, editable=False, db_index=True),
            preserve_default=False,
        ),
    ]
