from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from dictionary.views import dictionary_entry

def dictionary(request):
    context = {}
    if request.GET.get('q'):
        #return HttpResponse("adlfj")
        context = dictionary_entry(request)
        context['has_searched'] = True
    context['page'] = '_dictionary.html'
    return render(request, 'base.html', context)

def index(request):
    context = {}
    context['page'] = '_home.html'
    return render(request, 'base.html', context)

def search(request):
    query = request.GET['q']
    return HttpResponse("Hello World!")
