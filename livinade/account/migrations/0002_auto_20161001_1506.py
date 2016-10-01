# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 19:06
from __future__ import unicode_literals

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=account.models.avatar_upload_location),
        ),
        migrations.AlterField(
            model_name='profile',
            name='header_image',
            field=models.ImageField(blank=True, upload_to=account.models.header_upload_location),
        ),
    ]