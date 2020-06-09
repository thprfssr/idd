from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):

    if request.GET.get('q'):
        return HttpResponse("adlfj")

    return render(request, 'base.html')

def search(request):
    query = request.GET['q']
    return HttpResponse("Hello World!")
