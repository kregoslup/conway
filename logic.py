from collections import Counter


def ressurect(dots):
    neighbours = []
    d1 = dict()
    for x, y in dots:
        d1[(x, y)] = ((x+1, y+1), (x+1, y), (x, y+1), (x-1, y-1), (x-1, y),
                      (x, y-1), (x-1, y+1), (x+1, y-1))
    for key in d1:
        neighbours.extend(d1.get(key))
    c = Counter(neighbours)
    return c


def turn(c, dots):
    d = set(dots)
    for key in c:
        if c[key] not in [2, 3]:
            d.discard(key)
        if key not in dots and c[key] == 3:
            d.add(key)
    return d
