# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-20 16:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinemas', '0005_auto_20161120_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='movie_type',
        ),
    ]