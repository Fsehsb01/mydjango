from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from .models import lo


# Create your views here.
def lokk(request):
    return render(request, 'holle.html')
def look(request):
    name = request.POST.get('name')
    namet = request.POST.get('namet')
    if name==None and namet==None:
        return HttpResponse('1')
    else:
        lo.objects.create(name=name,namet=namet)

    return redirect(reverse('myweb:detail'))


def index(request):
    q = lo.objects.filter(stat__contains='1')
    print(lo.objects.filter(stat__contains='1'))
    return render(request, 'index.html', {'q': q})


def detail(request):
    q = lo.objects.filter(stat__contains='1')
    return render(request, 'myweb/detail.html', {'q': q})
