# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from dongycosts.utils import test_func
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from dongycosts.models import costs
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def list_costs(request):
    #test_func()
    CurrentUser = request.user
    username = CurrentUser.get_username()
    userid = User.objects.get(username=username)
    usercosts = costs.objects.filter(UserName=userid)
    NumberOfPayments = usercosts.__len__()
    list_data = {
        'NumberOfPayments':NumberOfPayments,
        'UserName':username,
        'usercosts':usercosts,
    }
    list_template = loader.get_template("lists.html")
    return HttpResponse(list_template.render(list_data,request))
