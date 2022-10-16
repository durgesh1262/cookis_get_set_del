from datetime import datetime, timedelta
from django.http import response
from django.shortcuts import render

# Create your views here.

def setcookie(request):
    response = render(request,'student/setcookie.html')
    response.set_cookie('kart','raj',expires=datetime.utcnow()+timedelta(days=2))
    return response

def getcookie(request):
    #nm = request.COOKIES['name']
    #nm = request.COOKIES.get('name')
    nm = request.COOKIES.get('kart','no cookies avilable..!')

    return render(request,'student/getcookie.html',{'name':nm})


def delcookie(request):
    response= render(request,'student/delcookie.html')
    response.delete_cookie('name')
    return response