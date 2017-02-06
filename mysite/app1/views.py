from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

def test(request):
    t=get_template('app1/test.html')
    info = dict(uid='gslee', phone= '5284', visits='23')
    html=t.render(Context(info))
    return HttpResponse(html)
def hello(request) :
    return HttpResponse('hi, Hello')
# Create your views here.
def index(request) :
    return HttpResponse('hi, index')

def login(request) :
    return HttpResponse('login')
def logout(request) :
    return HttpResponse('logout')
