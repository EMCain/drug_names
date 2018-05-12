import pickle
# based on http://www.onthelambda.com/2014/02/20/how-to-fake-a-sophisticated-knowledge-of-wine-with-markov-chains/
# but with letters instead of words


def generate_trigram(letters):
    if len(letters) < 3:
        return
    for i in range(len(letters) - 2):
        yield(letters[i], letters[i+1], letters[i+2])

chain = {}
with open('names.txt', 'r') as names:
    for line in names.readlines():
        line = '> ' + line
        for l1, l2, l3 in generate_trigram(line):
            key = (l1, l2)
            if key in chain:
                chain[key].append(l3)
            else:
                chain[key] = [l3]

pickle.dump(chain, open("chain.p", "wb" ))
# empty dict for markov chain
# open the file
# read the names
# process the names to markov chain dict

# use the markov chain generator to generate n drug names
