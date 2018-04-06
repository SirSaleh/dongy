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
    # obtain user object
    CurrentUser = request.user

    # get username
    username = CurrentUser.get_username()

    # get userid to get costs for user from costs model
    userid = User.objects.get(username=username)

    #get costs list
    usercosts = costs.objects.filter(UserName=userid)

    # get number of payments for user
    NumberOfPayments = usercosts.__len__()

    # context of lists template
    list_data = {
        'NumberOfPayments':NumberOfPayments,
        'UserName':username,
        'usercosts':usercosts,
    }

    # obtain template object
    list_template = loader.get_template("lists.html")
    
    return HttpResponse(list_template.render(list_data,request))
