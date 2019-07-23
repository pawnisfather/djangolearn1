from django.shortcuts import render

from .models import *


# Create your views here.
def index(request):
    book_list = BookInfo.objects.all()
    context = {'title': book_list}
    return render(request, 'booktest/index.html', context)


def show(request, id):
    # hero_info = HeroInfo.objects.get(pk=id)
    book = BookInfo.objects.get(pk=id)

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
