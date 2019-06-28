from django.shortcuts import render
from django.http import *
from django.template import loader, RequestContext
from .models import *


# Create your views here.
def index(request):
    book_list = BookInfo.objects.all()
    context = {'title': book_list}
    return render(request, 'booktest/index.html', context)
