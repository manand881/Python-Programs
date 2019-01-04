import itertools

a = 'dcab'
k = 4

for p in itertools.permutations(a, k):
    print ("".join(p)),