import string
import sys
from Spinner import Spinner

def clean_text(text):
    return text.translate(str.maketrans('', '', string.punctuation)).lower()

def main(synonym_file='test-synonyms.txt', essay_file='essay.txt'):
    spinner = Spinner(synonym_file)
    with open(essay_file, 'r') as f:
        original_text = clean_text(f.read())
        print("Original:", original_text)

        results = [original_text]
        for i in range(3):
            spun_text = spinner.spin_text(original_text)
            print(f"Option {i + 1}:", spun_text)
            results.append(spun_text)

    with open('results.txt', 'w') as f:
        for idx, result in enumerate(results):
            label = "Original" if idx == 0 else f"Option {idx}"
            f.write(f"{label}: {result}\n")

if __name__ == '__main__':
    synonym_file = sys.argv[1] if len(sys.argv) > 1 else 'test-synonyms.txt'
    essay_file = sys.argv[2] if len(sys.argv) > 2 else 'essay.txt'
    main(synonym_file, essay_file)
