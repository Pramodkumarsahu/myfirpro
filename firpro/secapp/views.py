from django.shortcuts import render
import datetime
from django.http import HttpResponse

# Create your views here.
def secapp_view(request):
    j=datetime.date.today()
    k=j.strftime('%d/%m/%Y')
    return HttpResponse('<h1>the local date is:'+str(k)+'</h1>')
