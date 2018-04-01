# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class friends (models.Model):
    Username = models.ForeignKey(User)
    FriendName = models.CharField(max_length=20)
    class Meta:
        unique_together = ('Username', 'FriendName',)

class costs (models.Model):
    CostId = models.AutoField(primary_key=True)
    UserName = models.ForeignKey(User)
    PayerName = models.CharField(max_length=20)
    FriendNames = models.CharField(max_length=20)
    FriendShare = models.CharField(max_length=1000)
    CostAmount = models.FloatField()
