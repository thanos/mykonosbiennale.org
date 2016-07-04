# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20160704_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='panel',
            name='slide_show',
            field=models.ForeignKey(default=3, blank=True, to='pages.SlideShow', null=True),
            preserve_default=False,
        ),
    ]
