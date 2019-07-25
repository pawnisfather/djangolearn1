from django.shortcuts import render
from django.http import HttpResponseRedirect as redirect
from .models import *


# Create your views here.
def index(request):
    book_list = BookInfo.objects.all()
    context = {'title': book_list}
    return render(request, 'booktest/index.html', context)


def show(request, id_s):
    # hero_info = HeroInfo.objects.get(pk=id)
    book = BookInfo.objects.get(pk=id_s)

    num_count = book.heroinfo_set.all()
    print(num_count.count())
    if num_count.count() == 0:
        print("没有")
        content = {"hero": None}
    else:
        print("有")
        content = {"hero": num_count}

    return render(request, 'booktest/show.html', content)


def year(request, year):
    content = {'year': year}
    return render(request, 'booktest/year.html', content)


def post(request):
    return render(request, 'booktest/postTest2.html')


def post2(request):
    print(request.method)
    print(request.POST)
    return render(request, 'booktest/postTest1.html', context=request.POST)


def session1(request):
    uname = request.session['myname']

    context = {'uname': uname}
    return render(request, 'booktest/session1.html', context=context)


def session2(request):
    return render(request, 'booktest/session2.html')


def session3(request):
    uname = request.POST['uname']
    request.session['myname'] = uname
    # print(request.session)
    return redirect('/booktest/login/')
    # return render(request, 'booktest/session3.html')

# def session4(requset):
#     del
