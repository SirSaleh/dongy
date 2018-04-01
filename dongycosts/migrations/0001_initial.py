# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-01 06:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='costs',
            fields=[
                ('CostId', models.AutoField(primary_key=True, serialize=False)),
                ('PayerName', models.CharField(max_length=20)),
                ('FriendNames', models.CharField(max_length=20)),
                ('FriendShare', models.FloatField()),
                ('CostAmount', models.FloatField()),
                ('UserName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='friends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FriendName', models.CharField(max_length=20)),
                ('Username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='friends',
            unique_together=set([('Username', 'FriendName')]),
        ),
    ]