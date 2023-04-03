import nltk
from nltk.corpus import wordnet as wn

nltk.app.wordnet()

a = wn.synsets('man')

seaside = wn.synsets('woman')
stack = 0
match = []
for i in seaside:
    for k in a:
        if stack <= i.path_similarity(k):
            stack = i.path_similarity(k)
            match.append(i)
            match.append(k)

print(match)