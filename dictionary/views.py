from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from dictionary.models import *

def dictionary_entry(request):
    query = request.GET.get('q')
    if query:
        #L = Lexicon()
        #L.load('lexicon.json')
        #search = L.search(query)
        if True:
            #c, d = search
            etymology = "Apo nevidonná originá"
            category = "n."
            definition = "alfjlajfjafj ladjfj ljaldfl jajf l"
            context = {'lemma': query, 'etymology': etymology, 'category': category, 'definition': definition}
            #return render(request, '_dictionary-entry.html', context)
        #else:
            #return HttpResponse("afal")
            return context
