import json
import requests

# Function to search for the definition of a word
def search_word(word):
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/{}".format(word)
    response = requests.get(url)
    data = json.loads(response.text)
    if 'title' in data:
        return data['title']
    else:
        meanings = []
        for result in data:
            for entry in result['meanings']:
                for definition in entry['definitions']:
                    meanings.append(definition['definition'])
        return '\n\n'.join(meanings)

# Function to save searched words to a JSON file
def save_words(word):
    with open('list2.txt', 'r+') as f:
        words = json.load(f)
        words.append(word,)
        f.seek(0)
        json.dump(words, f)

# Function to load searched words from a JSON file
def load_words():
    with open('list2.txt', 'r') as f:
        words = json.load(f)
        return words

# Main program loop
try:
    while True:
        print('Enter a word to search for its definition, or press Enter to quit.')
        word = input().strip().lower()
        if not word:
            break
        definition = search_word(word)
        print('\n\n'+ definition)
        save_words(word)
except KeyboardInterrupt as err:
    print('now quiting...')


