"""djtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# to add this file to your website:
# add this lines to your main urls.py
# from django.conf.urls import include
# url(r'^dongycosts/' ,include('dongycosts.urls')),

from django.conf.urls import url
from django.contrib import admin
from dongycosts import views as dongycosts_views

urlpatterns = [
    url(r'^$',dongycosts_views.index),
    url(r'^list/',dongycosts_views.list_costs),
    url(r'^balance/',dongycosts_views.show_balance),
    url(r'^EqualForm/',dongycosts_views.equal_form),
    url(r'^AddFriend/',dongycosts_views.add_friend),
]
