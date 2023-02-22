import itertools

def permutations(s):
    perms = itertools.permutations(s)
    return set(list(map(lambda x: "".join(x), perms)))
