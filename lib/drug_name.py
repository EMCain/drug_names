import json
import requests
from random import choice

BAD_WORDS_URL =  'https://www.cs.cmu.edu/~biglou/resources/bad-words.txt'
DRUG_NAMES = set()  # calclulate this the first time it runs

with open('names.txt', 'r') as f:
    for line in f.readlines():
        DRUG_NAMES.update({n for n in line.lower().strip().split()})

def create_drug_name():
    # Set a flag and loop until we find an inoffensive drug_name
    try:
        bad_words = get_bad_words(BAD_WORDS_URL)
    except:
        # Swallow exception if unable to connect and supply a list that won't
        # trip the profanity filter.
        bad_words = list('xyzabc')

    while True:
        drug_name = get_name_from_chain()
        if not is_offensive(drug_name, bad_words) and not is_duplicate(drug_name):
            return drug_name

def get_name_from_chain():
    with open('chain.json', 'r') as f:
        chain = json.load(f)
        new_name = ''

        l1 = '>'
        l2 = ' '

        while True:
            l1, l2 = l2, choice(chain[l1 + l2])
            if l2 == '\n':
                break
            new_name += l2
        return new_name

def is_duplicate(drug_name):
    if drug_name.lower() in DRUG_NAMES:
        return True  # accidentally generated a real drug name
    return False

def is_offensive(drug_name, bad_words):
    """ Check if any words in the specified list overlap with drug_name """

    for bad_word in bad_words:
        if bad_word in drug_name:
            return True
    return False

def get_bad_words(bad_words_url):
    """
    Retrieves a list of offensive words retrieved and parsed from
    the input url
    """
    r = requests.get(bad_words_url)

    if r.status_code != 200:
        raise requests.RequestException

    bad_words = r.text.strip().split("\n")
    return bad_words

# for testing
if __name__ == '__main__':
    print(create_drug_name())
