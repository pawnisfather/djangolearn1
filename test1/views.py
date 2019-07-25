from django.http import HttpResponse


# Create your views here.
def show(request, id):
    return HttpResponse(str(id))


def show1(request, ss,id):
    return HttpResponse(str(ss)+str(id))
