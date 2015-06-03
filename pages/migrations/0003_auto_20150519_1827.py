# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_panel_visibile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='visibile',
            new_name='visible',
        ),
        migrations.RenameField(
            model_name='panel',
            old_name='visibile',
            new_name='visible',
        ),
    ]
