# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-16 09:29
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AllLawyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('icon', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Lawyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, upload_to='lawyer_avatar/')),
                ('bio', models.TextField()),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('category', models.CharField(default='criminal', max_length=200)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='lawyer_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'All Lawyers',
            },
        ),
    ]
