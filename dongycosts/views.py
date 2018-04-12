# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from dongycosts.utils import test_func
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from dongycosts.models import costs
from dongycosts.models import friends
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# to addup dictionaries
from collections import Counter


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

@login_required
def show_balance(request):
    # obtain user object
    CurrentUser = request.user

    # get username
    username = CurrentUser.get_username()

    # get userid to get costs for user from costs model
    userid = User.objects.get(username=username)

    # get user friends
    userfriends = friends.objects.filter(Username=  userid)

    # get user friends FriendNames
    userfriendsnames = map(lambda x: x.FriendName,userfriends)

    # dictionary to store user blances
    # default is zero add add calculates for each payments
    UserBalances = {xx:0 for xx in userfriendsnames}

    #change UserBalances to counter for apply calculations
    UserBalances = Counter(UserBalances)

    #get costs list
    UserCosts = costs.objects.filter(UserName=userid)

    # get number of payments for user
    # NumberOfPayments = usercosts.__len__()

    for usercost in UserCosts:
        # Friend Names for specific payment (parsed)
        FriendNames = usercost.FriendNames.split(",")
        # Number of FriendShare
        FriendNumber = FriendNames.__len__()
        # Share of Frinds (not parsed)
        FriendShare = usercost.FriendShare
        # Total Cost Amount for a payment
        CostAmount = usercost.CostAmount
        # Name of the Payer
        PayerName = usercost.PayerName
        # chech if Friends share all equal (if There is no FriendShare)
        # for equal quota and non-equal quotas
        if FriendShare == None:
            FriendShare = [CostAmount/FriendNumber]*FriendNumber
        else:
            FriendShare = map(lambda xx: float(xx) ,FriendShare.split(",") )

        # Make FriendShare Negative for Calculations
        FriendShare = {value*-1 for value in FriendShare}

        # Dictionary of costs for current payment
        Current_cost_dic = dict(zip(FriendNames,FriendShare))

        # add up payer value to payer balance POSITIVELY
        UserBalances[PayerName] = UserBalances[PayerName] + CostAmount

        # add up payer value to payer balance NEGATIVELY
        UserBalances.update(Counter(Current_cost_dic))
        #UserBalances = dict( Counter(UserBalances) + Counter(Current_cost_dic))

    print(UserBalances)
    return HttpResponse("<h1> This is Balance Page </h1> just printed in console.")
