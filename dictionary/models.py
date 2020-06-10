from django.db import models

import json

DEFAULT_ETYMOLOGY = 'Apo nevidonná originá.'

# This function takes a string, and converts any square brackets into
# HTML italic tags. Also, `seniská greciská` is replaced with a link to the
# Wikipedia page for Ancient Greek.
def parse_string(s):
    s = s.replace('[', '<i>').replace(']', '</i>')
    s = s.replace('seniská greciská', '<a href="https://en.wikipedia.org/wiki/Ancient_Greek">seniská greciská</a>')
    s = s.replace('latiniská', '<a href="https://en.wikipedia.org/wiki/Latin">latiniská</a>')
    s = s.replace('proto-indo-europiská', '<a href="https://en.wikipedia.org/wiki/Proto-Indo-European_language">proto-indo-europiská</a>')
    return s

class Lexicon:
    def __init__(self):
        self.database = {}


    # If the lemma is not in the dictionary, then this function creates it.
    # If the lemma already exists with N definitions, and the i is in the
    # interval [1, N], then the i-th definition is modified.
    # If the i is not within the interval [1, N], then a new definition is
    # appended.
    def set_definition(self, lemma, category = '', definition = '', example = '', i = 0):
        if lemma not in self.database.keys():
            # We cannot create an entry with empty category or definition
            if category == '' or definition == '':
                return

            self.database[lemma] = {'categories': [], 'definitions': [], 'examples': []}

            self.database[lemma]['categories'].append(category)
            self.database[lemma]['definitions'].append(definition)
            self.database[lemma]['examples'].append(example)

        elif 1 <= i <= len(self.database[lemma]['categories']):
            # If the passed parameters are empty, then we do not modify them.
            if len(category) != 0:
                self.database[lemma]['categories'][i - 1] = category
            if len(definition) != 0:
                self.database[lemma]['definitions'][i - 1] = definition
            if len(example) != 0:
                self.database[lemma]['examples'][i - 1] = example
        else:
            self.database[lemma]['categories'].append(category)
            self.database[lemma]['definitions'].append(definition)
            self.database[lemma]['examples'].append(example)

    # Delete the i-th definition. If i is out of range, don't do anything.
    def delete_definition(self, lemma, i):
        if lemma not in self.database.keys():
            return

        if 1 <= i <= len(self.database[lemma]['categories']):
            del self.database[lemma]['categories'][i - 1]
            del self.database[lemma]['definitions'][i - 1]
            del self.database[lemma]['examples'][i - 1]

    # Delete lemma
    def delete_lemma(self, lemma):
        if lemma not in self.database.keys():
            return
        del self.database[lemma]

    def set_etymology(self, lemma, etymology):
        self.database[lemma]['etymology'] = etymology

    def dump(self):
        print(json.dumps(self.database))

    def save(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.database, f)

    def load(self, filename):
        with open(filename, 'r') as f:
            self.database = json.load(f)

    # Return dictionary entries which satisfy a query
    def search(self, query):
        matches = Lexicon()
        for lemma in self.database.keys():
            categories = self.database[lemma]['categories']
            definitions = self.database[lemma]['definitions']
            is_match = False
            if query in lemma:
                is_match = True
            for i in range(0, len(categories)):
                if query in definitions[i]:
                    is_match = True
            if is_match:
                matches.database[lemma] = self.database[lemma]
        return matches
                    


    def search_lemma(self, lemma):
        return lemma in self.database.keys()
