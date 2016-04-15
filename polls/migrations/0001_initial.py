# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-15 13:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gundem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gundem_adi', models.CharField(max_length=200, verbose_name='G\xfcndemin Ad\u0131')),
                ('olusturulma_tarihi', models.DateTimeField(auto_now_add=True, null=True)),
                ('gundem_tarihi', models.DateField(verbose_name='G\xfcndemin Tarihi')),
                ('gorusler', models.TextField(max_length=255, verbose_name='G\xf6r\xfc\u015fler')),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('ekleyen_kullanici', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'G\xfcndem Hadiseleri',
            },
        ),
        migrations.CreateModel(
            name='MailList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('olusturulma_tarihi', models.DateTimeField(auto_now_add=True, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Mail Listesi',
            },
        ),
        migrations.CreateModel(
            name='OnemDerecesi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('derece', models.CharField(max_length=60, verbose_name='\xd6nem Derecesi')),
                ('olusuturlma_tarihi', models.DateTimeField(auto_now_add=True, null=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': '\xd6nem Dereceleri',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefon', models.CharField(max_length=17, verbose_name='Telefon')),
                ('tanim', models.CharField(max_length=150, verbose_name='Tan\u0131m')),
                ('slug', models.SlugField(unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Kullan\u0131c\u0131lar',
            },
        ),
        migrations.AddField(
            model_name='gundem',
            name='onem_derecesi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.OnemDerecesi'),
        ),
        migrations.AddField(
            model_name='gundem',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Etiketler'),
        ),
    ]