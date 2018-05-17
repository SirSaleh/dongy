from __future__ import unicode_literals
from django.template import loader
from django.shortcuts import redirect

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# views
@login_required
def index(request):
    '''
        check if User is_authenticated
        Authenticated Users will be redirected to
        dongy_costs apps, Others should authenticate
    '''
    if request.user.is_authenticated:
        return redirect('dongy_index')

    return redirect('login')
