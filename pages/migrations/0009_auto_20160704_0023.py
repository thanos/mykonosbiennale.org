# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_panel_slide_show'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panel',
            name='slide_show',
            field=models.ForeignKey(default=None, blank=True, to='pages.SlideShow', null=None),
        ),
    ]
