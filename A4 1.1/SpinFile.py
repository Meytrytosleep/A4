import string

def clean_text(text):
    return text.translate(str.maketrans('', '', string.punctuation)).lower()

def main():
    spinner = Spinner('test-synonyms.txt')
    with open('essay.txt', 'r') as f:
        original_text = clean_text(f.read())
        print("Original:", original_text)
        for i in range(3):
            spun_text = spinner.spin_text(original_text)
            print(f"Option {i + 1}:", spun_text)

if __name__ == '__main__':
    main()
