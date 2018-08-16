import json
from random import choice


def create_drug_name():
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

# for testing
if __name__ == '__main__':
    print(create_drug_name())
