# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 03:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20161003_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
