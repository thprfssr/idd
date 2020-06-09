from django.db import models

# Create your models here.

import json

class Lexicon:
    def __init__(self):
        self.database = {}

    def add(self, lemma, category, definition):
        self.database[lemma] = {"category": category, "definition": definition}

    def print(self):
        for lemma in sorted(self.database.keys()):
            category = self.database[lemma]["category"]
            definition = self.database[lemma]["definition"]
            print("%s (%s): %s" % (lemma, category, definition))

    def dump(self):
        print(json.dumps(self.database))

    def save(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.database, f)

    def load(self, filename):
        with open(filename, 'r') as f:
            self.database = json.load(f)

    def search(self, lemma):
        if lemma in self.database:
            category = self.database[lemma]["category"]
            definition = self.database[lemma]["definition"]
            return (category, definition)
        else:
            return None
