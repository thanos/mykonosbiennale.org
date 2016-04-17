# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('filmfestival', '0025_auto_20150616_0309'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='contact_email',
            field=models.EmailField(default=b'', max_length=254, blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='contact_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default=b'', max_length=128, blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='posted_on_facebook',
            field=models.BooleanField(default=False),
        ),
    ]
