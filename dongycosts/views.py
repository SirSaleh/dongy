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
# to load forms
from dongycosts.forms import EqualForm
from dongycosts.forms import Add_Friend_Form



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

    # friends Number
    userfriends_Number = userfriends.__len__()

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
    NumberOfPayments = UserCosts.__len__()

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
        FriendShare = [value*-1 for value in FriendShare]

        # Dictionary of costs for current payment
        Current_cost_dic = dict(zip(FriendNames,FriendShare))

        # add up payer value to payer balance POSITIVELY
        UserBalances[PayerName] = UserBalances[PayerName] + CostAmount

        # add up payer value to payer balance NEGATIVELY
        UserBalances.update(Counter(Current_cost_dic))

    # Load template for Balances
    Balance_Template = loader.get_template('balance.html')

    # Context for Balance Tempalate
    Balance_Context = {
        'UserName':username,
        'NumberOfPayments':NumberOfPayments,
        'UserBalances':dict(UserBalances),
        'userfriends_Number':userfriends_Number,
    }

    return HttpResponse(Balance_Template.render(Balance_Context,request))

@login_required
def equal_form(request):
    # obtain user object
    CurrentUser = request.user

    # get username
    username = CurrentUser.get_username()

    # get userid to get costs for user from costs model
    userid = User.objects.get(username=username)

    # get Friends
    Friends = friends.objects.filter(Username = userid)

    # get Number of Friend
    Friends_Number = Friends.__len__()

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EqualForm(request.POST,userid=userid)
        # check whether it's valid:
        if form.is_valid():
            # Get name of Payer
            PayerName = request.POST.get('PayerName')

            # Users of current payment
            FriendNames = request.POST.getlist('FriendNames')
            # Change the list of users to
            #   comma seperated form in order to saving in database
            FriendNames = ",".join(FriendNames)

            # Total Cost Amount for current Payments
            CostAmount = float(request.POST.getlist('CostAmount')[0])

            # Instance for Current Payment Query
            PaymentInstance = costs(UserName = CurrentUser, PayerName = PayerName, FriendNames = FriendNames,CostAmount = CostAmount )
            PaymentInstance.save()
            # ...
            # redirect to a new URL:
            return HttpResponse("<h1> Thanks </h1>")

    # if a GET
    else:
        form = EqualForm(userid=userid)


    Form_Template = loader.get_template("forms.html")

    # forms context
    Form_Context = {
        'title':'Add a Payment',
        'form':EqualForm(userid=userid),
        'UserName':username,
        'Friends_Number':Friends_Number,
    }

    return HttpResponse(Form_Template.render(Form_Context,request))

@login_required
def add_friend(request):
    # obtain user object
    CurrentUser = request.user

    # get username
    username = CurrentUser.get_username()

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # Get name of Payer
        NewFriendName = request.POST.get('NewFriendName')

        # check if it not exists Before
        oldfriends = friends.objects.filter(Username=CurrentUser)
        oldfriends = [x.FriendName for x in oldfriends]
        if (NewFriendName in oldfriends):
            return HttpResponse("<h1> Sorry</h1>You Registered this friend's Name before.")

        # create a form instance and populate it with data from the request:
        form = Add_Friend_Form(request.POST)
        print("Before Check valid")
        # check whether it's valid:
        if form.is_valid():

            # Instance for Current Payment Query
            NewFriendInstance = friends(Username=CurrentUser,FriendName=NewFriendName)
            NewFriendInstance.save()
            # ...
            #
            return HttpResponse("<h1> Thanks </h1> Your new Friend <span style='color:red;'>"+NewFriendName+
                "</span> added successfully.<br> <a href='"+request.path+"'>Back to Add friends page. </a>")

    # if a GET
    else:
        form = Add_Friend_Form()

    # Context of add friend page
    Add_Friend_Context = {
        'title':'Add a Friend',
        'UserName':username,
        'form':Add_Friend_Form(),
    }

    # get template of forms
    Forms_Template = loader.get_template('forms.html')

    return HttpResponse(Forms_Template.render(Add_Friend_Context,request))

@login_required
def index (request):
    # obtain user object
    CurrentUser = request.user

    # get username
    username = CurrentUser.get_username()

    # get userid to get costs for user from costs model
    userid = User.objects.get(username=username)

    # get Friends
    Friends = friends.objects.filter(Username = userid)

    # get Number of Friend
    Friends_Number = Friends.__len__()

    # get index template
    index_Template = loader.get_template("index.html")

    index_context = {
        'UserName': username,
        'Friends_Number':Friends_Number,
    }

    return (HttpResponse(index_Template.render(index_context,request)))
