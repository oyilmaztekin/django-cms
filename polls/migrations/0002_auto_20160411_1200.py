# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 12:00
from __future__ import unicode_literals

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='maillist',
            options={'verbose_name_plural': 'Mail Listesi'},
        ),
        migrations.AlterModelOptions(
            name='onemderecesi',
            options={'verbose_name_plural': '\xd6nem Dereceleri'},
        ),
        migrations.AlterField(
            model_name='gundem',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Etiketler'),
        ),
    ]
