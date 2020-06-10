from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from dictionary.views import dictionary_entry

def index(request):
    context = None
    if request.GET.get('q'):
        #return HttpResponse("adlfj")
        context = dictionary_entry(request)
        context['has_searched'] = True

    return render(request, 'base.html', context)

def search(request):
    query = request.GET['q']
    return HttpResponse("Hello World!")
