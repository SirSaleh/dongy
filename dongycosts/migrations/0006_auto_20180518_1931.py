# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-18 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dongycosts', '0005_auto_20180518_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='ProfileId',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]