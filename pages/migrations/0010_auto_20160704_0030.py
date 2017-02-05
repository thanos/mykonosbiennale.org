# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20160704_0023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slide',
            name='slide_show',
        ),
        migrations.RemoveField(
            model_name='panel',
            name='slide_show',
        ),
        migrations.DeleteModel(
            name='Slide',
        ),
        migrations.DeleteModel(
            name='SlideShow',
        ),
    ]
