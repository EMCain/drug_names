from random import choice

import constants as c
from drug_name import create_drug_name
from generate_disease import disease


def get_ad():
    question = choice(c.QUESTIONS).format(disease())
    answer = choice(c.ANSWERS).format(create_drug_name())

    return '{} {}'.format(question, answer)


# for testing
if __name__ == '__main__':
    print(get_ad())
