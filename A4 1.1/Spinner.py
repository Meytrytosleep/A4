import random

class Spinner:
    def __init__(self, synonym_file, spin_probability=50):
        self.synonyms = self._load_synonyms(synonym_file)
        self.spin_probability = spin_probability

    def _load_synonyms(self, filename):
        synonyms = {}
        with open(filename, 'r') as f:
            for line in f.readlines():
                key, values = line.strip().split(':')
                synonyms[key] = values.split(', ')
        return synonyms

    def set_spin_probability(self, probability):
        """Sets the probability of a word being spun to a synonym."""
        self.spin_probability = probability

    def spin_word(self, word, previous_word):
        if previous_word == "very":
            return word

        if word in self.synonyms:
            if random.randint(1, 100) > self.spin_probability:
                return random.choice(self.synonyms[word])
        return word

    def spin_text(self, text):
        words = text.split()
        spun_words = []
        for idx, word in enumerate(words):
            previous_word = words[idx-1] if idx > 0 else None
            spun_words.append(self.spin_word(word, previous_word))
        return ' '.join(spun_words)
