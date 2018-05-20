import pickle
from random import choice


def create_drug_name():
    chain = pickle.load(open("chain.p", "rb"))

    new_name = ''

    l1 = '>'
    l2 = ' '

    while True:
        l1, l2 = l2, choice(chain[(l1, l2)])
        if l2 == '\n':
            break
        new_name += l2

    return new_name
