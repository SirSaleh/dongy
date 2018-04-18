from django import forms
from django.contrib.auth.models import User
from dongycosts.models import friends

# TODO solve request not found
# obtain user object
#CurrentUser = request.user

# get username
#username = CurrentUser.get_username()

# get userid to get costs for user from costs model
#userid = User.objects.get(username=username)

#UserFriends = friends.objects.filter(Username = userid)

#CHOICES = {xx.FriendName for xx in UserFriends}
#print("here")
#print (CHOICES)
#CHOICES = {(xx,xx) for xx in list(CHOICES)}

class EqualForm (forms.Form):
    CHOICES = ()
    # initiall the form class fields with friends name
    def __init__(self,*args,**kwargs):
        userid = kwargs.pop('userid')
        super(EqualForm, self).__init__(*args, **kwargs)

        UserFriends = friends.objects.filter(Username = userid)

        self.CHOICES = {xx.FriendName for xx in UserFriends}

        self.CHOICES = {(xx,xx) for xx in list(self.CHOICES)}

        ##
        # set choices to payer and users for a payment
        ##
        self.fields['PayerName'].choices =  self.CHOICES

        self.fields['FriendNames'].choices =  self.CHOICES


    # payer name, single choice to determine who payed for current payment
    PayerName = forms.ChoiceField(widget=forms.RadioSelect())

    # list of Friends name who uses current payment.
    FriendNames = forms.MultipleChoiceField(
            label="Friend Names",
            required=True,
            widget=forms.CheckboxSelectMultiple())

    # amount of the current payment
    CostAmount = forms.FloatField(min_value=0,label="Cost Amount")

class Add_Friend_Form(forms.Form):
    NewFriendName = forms.CharField(max_length=20,label="New Friend Name")
