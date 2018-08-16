from random import choice, randint
import constants as c


def adj_organ():
    return '{} {}'.format(
        choice(c.ADJECTIVES),
        choice(c.BODY_PARTS)
    )


def color_bile():
    return 'an excess of {} bile'.format(
        choice(c.COLORS).lower()
    )


def superlative_symptom():
    return '{} {}'.format(
        choice(c.SUPERLATIVES),
        choice(c.SYMPTOMS)
    )


def disease():
    index = randint(0, 5)
    if index == 0:
        return color_bile()
    elif index == 1:
        return superlative_symptom()
    else:
        return adj_organ()


# for testing
if __name__ == '__main__':
    print(disease())
