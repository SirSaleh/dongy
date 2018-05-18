# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class friends (models.Model):
    Username = models.ForeignKey(User,on_delete=models.CASCADE)
    ProfileID = models.ForeignKey('dongycosts.profiles',on_delete=models.CASCADE)
    FriendName = models.CharField(max_length=20)
    ProfileID = models.IntegerField(default=1)
    class Meta:
        unique_together = (('Username', 'FriendName','ProfileID'))

class costs (models.Model):
    CostId = models.AutoField(primary_key=True)
    UserName = models.ForeignKey(User,on_delete=models.CASCADE)
    PayerName = models.CharField(max_length=20)
    FriendNames = models.CharField(max_length=20)
    FriendShare = models.CharField(max_length=1000,null=True,blank=True)
    CostAmount = models.FloatField()

class profiles (models.Model):
    ProfileId = models.IntegerField(primary_key=True)
    Username = models.ForeignKey(User,on_delete=models.CASCADE)
    ProfileName = models.CharField(max_length=20)
