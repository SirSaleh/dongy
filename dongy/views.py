from __future__ import unicode_literals
from django.template import loader


from django.shortcuts import render
from django.http import HttpResponse

# views
def index(request):
    index_template = loader.get_template("index.html")
    return HttpResponse(index_template.render({},request))
