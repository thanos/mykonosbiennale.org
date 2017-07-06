# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import versatileimagefield.fields
import django_countries.fields
import phonenumber_field.modelfields
import tagulous.models.models
import tagulous.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('sort_by', models.CharField(max_length=100, null=True, blank=True)),
                ('slug', models.SlugField(max_length=200, null=True, blank=True)),
                ('text', models.TextField(default=b'', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Festival',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('sort_by', models.CharField(max_length=100, null=True, blank=True)),
                ('slug', models.SlugField(max_length=200, null=True, blank=True)),
                ('text', models.TextField(default=b'', blank=True)),
                ('year', models.IntegerField(default=2015)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FestivalProject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('sort_by', models.CharField(max_length=100, null=True, blank=True)),
                ('slug', models.SlugField(max_length=200, null=True, blank=True)),
                ('text', models.TextField(default=b'', blank=True)),
                ('festival', models.ForeignKey(to='festivaly.Festival')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('sort_by', models.CharField(max_length=100, null=True, blank=True)),
                ('slug', models.SlugField(max_length=200, null=True, blank=True)),
                ('text', models.TextField(default=b'', blank=True)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to=b'material/', null=True, verbose_name=b'image', blank=True)),
                ('video', models.FileField(max_length=256, null=True, upload_to=b'material/', blank=True)),
                ('src', models.TextField(default=b'', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('sort_by', models.CharField(max_length=100, null=True, blank=True)),
                ('slug', models.SlugField(max_length=200, null=True, blank=True)),
                ('text', models.TextField(default=b'', blank=True)),
                ('email', models.EmailField(default=b'', max_length=254, blank=True)),
                ('country', django_countries.fields.CountryField(default=b'', max_length=2, blank=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(default=b'', max_length=128, blank=True)),
                ('bio', models.TextField(default=b'', blank=True)),
                ('statement', models.TextField(default=b'', blank=True)),
                ('facebook', models.CharField(max_length=100)),
                ('twitter', models.CharField(max_length=100)),
                ('instagram', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('sort_by', models.CharField(max_length=100, null=True, blank=True)),
                ('slug', models.SlugField(max_length=200, null=True, blank=True)),
                ('text', models.TextField(default=b'', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('slug', models.SlugField()),
                ('count', models.IntegerField(default=0, help_text='Internal counter of how many times this tag is in use')),
                ('protected', models.BooleanField(default=False, help_text='Will not be deleted when the count reaches 0')),
                ('path', models.TextField(unique=True)),
                ('label', models.CharField(help_text='The name of the tag, without ancestors', max_length=255)),
                ('level', models.IntegerField(default=1, help_text='The level of the tag in the tree')),
                ('parent', models.ForeignKey(related_name='children', blank=True, to='festivaly.Tag', null=True)),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
            bases=(tagulous.models.models.BaseTagTreeModel, models.Model),
        ),
        migrations.CreateModel(
            name='Art',
            fields=[
                ('album_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='festivaly.Album')),
            ],
            options={
                'abstract': False,
            },
            bases=('festivaly.album',),
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('participation_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='festivaly.Participation')),
                ('artwork', models.ManyToManyField(related_name='artist', to='festivaly.Art')),
            ],
            bases=('festivaly.participation',),
        ),
        migrations.CreateModel(
            name='FilmDirector',
            fields=[
                ('participation_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='festivaly.Participation')),
            ],
            bases=('festivaly.participation',),
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('participation_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='festivaly.Participation')),
            ],
            bases=('festivaly.participation',),
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=tagulous.models.fields.TagField(autocomplete_view=b'festivalA_tag_autocomplete', default=b'', initial=b'2013, 2013/artist, 2015', tree=True, force_lowercase=True, to='festivaly.Tag', blank=True, help_text='Enter a comma-separated tag string', _set_tag_meta=True),
        ),
        migrations.AddField(
            model_name='participation',
            name='festival_project',
            field=models.ForeignKey(to='festivaly.FestivalProject'),
        ),
        migrations.AddField(
            model_name='participation',
            name='participant',
            field=models.ForeignKey(to='festivaly.Participant'),
        ),
        migrations.AddField(
            model_name='participant',
            name='albumn',
            field=models.ForeignKey(blank=True, to='festivaly.Album', null=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='tags',
            field=tagulous.models.fields.TagField(autocomplete_view=b'festivalA_tag_autocomplete', default=b'', initial='2013, 2013/artist, 2015', tree=True, force_lowercase=True, to='festivaly.Tag', blank=True, help_text='Enter a comma-separated tag string', _set_tag_meta=True),
        ),
        migrations.AddField(
            model_name='media',
            name='tags',
            field=tagulous.models.fields.TagField(autocomplete_view=b'festivalA_tag_autocomplete', default=b'', initial='2013, 2013/artist, 2015', tree=True, force_lowercase=True, to='festivaly.Tag', blank=True, help_text='Enter a comma-separated tag string', _set_tag_meta=True),
        ),
        migrations.AddField(
            model_name='festivalproject',
            name='project',
            field=models.ForeignKey(to='festivaly.Project'),
        ),
        migrations.AddField(
            model_name='festivalproject',
            name='tags',
            field=tagulous.models.fields.TagField(autocomplete_view=b'festivalA_tag_autocomplete', default=b'', initial='2013, 2013/artist, 2015', tree=True, force_lowercase=True, to='festivaly.Tag', blank=True, help_text='Enter a comma-separated tag string', _set_tag_meta=True),
        ),
        migrations.AddField(
            model_name='festival',
            name='tags',
            field=tagulous.models.fields.TagField(autocomplete_view=b'festivalA_tag_autocomplete', default=b'', initial=b'2013, 2013/artist, 2015', tree=True, force_lowercase=True, to='festivaly.Tag', blank=True, help_text='Enter a comma-separated tag string', _set_tag_meta=True),
        ),
        migrations.AddField(
            model_name='album',
            name='media',
            field=models.ManyToManyField(related_name='album', to='festivaly.Media'),
        ),
        migrations.AddField(
            model_name='album',
            name='tags',
            field=tagulous.models.fields.TagField(autocomplete_view=b'festivalA_tag_autocomplete', default=b'', initial=b'2013, 2013/artist, 2015', tree=True, force_lowercase=True, to='festivaly.Tag', blank=True, help_text='Enter a comma-separated tag string', _set_tag_meta=True),
        ),
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together=set([('slug', 'parent')]),
        ),
    ]
