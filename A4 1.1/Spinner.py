import random

class Spinner:
    def __init__(self, synonym_file, spin_probability=50):
        self.synonyms = self._load_synonyms(synonym_file)
        self.spin_probability = spin_probability

    def _load_synonyms(self, filename):
        synonyms = {}
        try:
            with open(filename, 'r') as f:
                for line in f.readlines():
                    key, values = line.strip().split(':')
                    synonyms[key] = values.split(', ')
        except Exception as e:
            print(f"Error reading synonym file: {e}")
        return synonyms

    def spin_word(self, word):
        if word in self.synonyms and random.randint(1, 100) > self.spin_probability:
            synonyms = [syn for syn in self.synonyms[word] if syn != word]
            return random.choice(synonyms) if synonyms else word
        return word

    def spin_text(self, text):
        return ' '.join([self.spin_word(word) for word in text.split()])
