from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request) :
   # return HttpResponse("Hello World!!") 
   return render(request,'home.html',{'name':'Ammu'})

def add(request) :
    num1 = int(request.GET['num1'])  # default data type is String
    num2 = int(request.GET['num2'])
    res = num1 + num2
    return render(request,'results.html',{'result':res})