# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 00:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
    ]
