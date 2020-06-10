from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from dictionary.models import *
"""
def dictionary_entry(request):
    query = request.GET.get('q')
    if query:
        L = Lexicon()
        L.load('dictionary/lexicon.json')
        search = L.search(query)
        if search:
            #c, d = search
            etymology = "Apo nevidonná originá"
            category, definition = search
            context = {'lemma': query, 'etymology': etymology, 'category': category, 'definition': definition}
            #return render(request, '_dictionary-entry.html', context)
        #else:
            #return HttpResponse("afal")
            return context
"""

def dictionary_entry(request):
    query = request.GET.get('q')
    if query:
        L = Lexicon()
        L.load('dictionary/lexicon.json')
        matches = L.search(query)

        matches_list = []
        for lemma in sorted(matches.database.keys()):
            categories = matches.database[lemma]['categories']
            definitions = matches.database[lemma]['definitions']
            examples = matches.database[lemma]['examples']
            entries = []
            for i in range(0, len(categories)):
                entry = {'category': categories[i], 'definition': definitions[i], 'example': examples[i]}
                entries.append(entry)
            #matches_list.append({'lemma': lemma, 'categories': categories, 'definitions': definitions, 'examples': examples, 'range': range(0, len(categories))})
            etymology = matches.database[lemma]['etymology']
            matches_list.append({'lemma': lemma, 'entries': entries, 'etymology': etymology})

        context = {'matches': matches_list}

    return context
