import random

class Spinner:
    def __init__(self, synonym_file):
        self.synonyms = self._load_synonyms(synonym_file)

    def _load_synonyms(self, filename):
        synonyms = {}
        with open(filename, 'r') as f:
            for line in f.readlines():
                key, values = line.strip().split(':')
                synonyms[key] = values.split(', ')
        return synonyms

    def spin_word(self, word):
        if word in self.synonyms:
            if random.randint(1, 100) > 50:
                return random.choice(self.synonyms[word])
        return word

    def spin_text(self, text):
        words = text.split()
        return ' '.join([self.spin_word(word) for word in words])
