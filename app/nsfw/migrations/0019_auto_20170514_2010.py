# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-05-14 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nsfw', '0018_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='lon',
            field=models.FloatField(blank=True, null=True),
        ),
    ]