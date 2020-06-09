from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from dictionary.models import *

def dictionary_entry(request):
    query = request.GET.get('q')
    if query:
        L = Lexicon()
        L.load('lexicon.json')
        search = L.search(query)
        if search:
            c, d = search
            context = {lemma: query, etymology = "Apo nevidonná originá", category: c, definition: d}
            return render(request, '_dictionary-entry.html', context)
        else:
            HttpResponse("afal")
