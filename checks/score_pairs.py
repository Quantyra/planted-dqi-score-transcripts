"""Exact GF(4), k=2 audit of the pair kernel and the reused-table histogram."""

from collections import Counter
from itertools import combinations, product
from math import comb


FIELD = range(4)
MULTIPLY = (
    (0, 0, 0, 0), (0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)
)
POLYNOMIALS = [
    tuple(a ^ MULTIPLY[b][x] for x in FIELD) for a, b in product(FIELD, repeat=2)
]
LISTS = list(combinations(FIELD, 2))


def verify(planted, reference):
    choices = [[row for row in LISTS if not planted or value in row]
               for value in reference]
    observed = Counter()
    tables = 0
    for table in product(*choices):
        tables += 1
        histogram = Counter(sum(y in row for y, row in zip(values, table))
                            for values in POLYNOMIALS)
        assert sum(n * (1 + (score - 2) ** 2)
                   for score, n in histogram.items()) == 2 * len(POLYNOMIALS)
        for s, n in histogram.items():
            for t, count in histogram.items():
                observed[s, t] += n * count

    # Colors keep only the equalities among A(x), C(x), and the reference.
    # Independently recover row hit counts from representatives of each color.
    representatives = {
        (True, True, True): (0, 0), (True, False, False): (0, 1),
        (False, True, False): (1, 0), (False, False, True): (1, 1),
        (False, False, False): (1, 2),
    }
    kernels = {color: Counter((int(a in row), int(c in row)) for row in LISTS
                              if not planted or 0 in row)
               for color, (a, c) in representatives.items()}
    patterns = Counter(tuple((a == p, c == p, a == c)
                             for a, c, p in zip(left, right, reference))
                       for left, right in product(POLYNOMIALS, repeat=2))
    reconstructed = Counter()
    for colors, multiplicity in patterns.items():
        scores = {(0, 0): multiplicity}
        for color in colors:
            updated = Counter()
            for (s, t), count in scores.items():
                for (ds, dt), ways in kernels[color].items():
                    updated[s + ds, t + dt] += count * ways
            scores = updated
        reconstructed.update(scores)

    assert reconstructed == observed
    assert sum(observed.values()) == tables * len(POLYNOMIALS) ** 2
    # Two independent functions have four equally probable bit pairs per row
    # conditional on any balanced table. Check their common envelope mass.
    assert sum(comb(4, s) * (1 + (s - 2) ** 2) for s in range(5)) == 32
    return tables


if __name__ == "__main__":
    print("NO tables:", verify(False, POLYNOMIALS[0]))
    print("YES tables, zero plant:", verify(True, POLYNOMIALS[0]))
    print("YES tables, nonconstant plant:", verify(True, POLYNOMIALS[6]))
