# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-20 16:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinemas', '0009_auto_20161120_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='screening',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='cinema',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='movie_type',
        ),
        migrations.DeleteModel(
            name='Cinema',
        ),
        migrations.DeleteModel(
            name='Screening',
        ),
    ]