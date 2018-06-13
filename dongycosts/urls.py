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

from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from dongycosts import views as dongycosts_views
# class-based ViewSets
from dongycosts.views import About
# for Use in REST API
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)



urlpatterns = [
    url(r'^$',dongycosts_views.index,name= "dongy_index"),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^list/',dongycosts_views.list_costs,name="dongy_list"),
    url(r'^balance/',dongycosts_views.show_balance,name= "dongy_balance"),
    url(r'^EqualForm/',dongycosts_views.equal_form,name="dongy_equalform"),
    url(r'^AddFriend/',dongycosts_views.add_friend,name="dongy_addFriend"),
    url(r'^about/',About.as_view()),
]
