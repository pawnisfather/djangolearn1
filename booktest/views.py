from django.shortcuts import render
from django.http import *


# Create your views here.
def index(request):
    print(request.get_port())
    return HttpResponse('hello world')
