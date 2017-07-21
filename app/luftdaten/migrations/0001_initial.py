# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-08 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SensorValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SDS_P1', models.FloatField()),
                ('SDS_P2', models.FloatField()),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('samples', models.FloatField()),
                ('min_micro', models.FloatField()),
                ('max_micro', models.FloatField()),
                ('signal', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]