import json


def generate_trigram(letters):
    if len(letters) < 3:
        return
    for i in range(len(letters) - 2):
        yield(letters[i], letters[i + 1], letters[i + 2])


chain = {}
with open('names.txt', 'r') as names:
    for line in names.readlines():
        line = '> ' + line
        for l1, l2, l3 in generate_trigram(line):
            key = l1 + l2
            if key in chain:
                chain[key].append(l3)
            else:
                chain[key] = [l3]

    with open('chain.json', 'w') as outfile:
        json.dump(chain, outfile, indent=4, sort_keys=True)
