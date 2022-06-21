from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import lo


# Create your views here.
def look(request):
    name = request.POST.get('name')
    namet = request.POST.get('namet')
    if name==''and namet=='' :
        return HttpResponse('至少要一个有东西吧')
    else:
        lo.objects.filter(name=name, namet=namet).first()
        lo.objects.create(name=name, namet=namet)
        return render(request, 'holle.html')


def index(request):
    q = lo.objects.filter(stat='1')

    return render(request, 'index.html', {'q': q})


def detail(request):
    q=lo.objects.all()
    return render(request, 'myweb/detail.html', {'q': q})
