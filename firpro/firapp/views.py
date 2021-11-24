from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def firapp_view(request):
    t=datetime.datetime.today()
    j=t.strftime('%I:%M:%S---%d/%m/%Y')
    s='<h1> the local date & time is :'+str(j)+'</h1>'
    return HttpResponse(s)
