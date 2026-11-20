"""Integer Fourier checks and exact first moments for the random-table screen."""

from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import comb, isqrt
from random import Random

from finite_field import Field, walsh


def evaluate(field, a, x, k):
    result = 0
    for j in reversed(range(k)):
        coefficient = (a >> (j * field.b)) & (field.q - 1)
        result = field.mul(result, x) ^ coefficient
    return result


def frequency_support(field, k):
    """Indices for Walsh on the binary representation of coefficients."""
    row_modes = []
    for x in range(field.q):
        modes = []
        for u in range(1, field.q):
            mask = 0
            for i in range(field.b * k):
                value = evaluate(field, 1 << i, x, k)
                mask |= field.trace[field.mul(u, value)] << i
            modes.append(mask)
        row_modes.append(modes)
    reached = {0}
    for t in range(1, k // 2 + 1):
        for selected in combinations(row_modes, t):
            for modes in product(*selected):
                frequency = 0
                for mode in modes:
                    frequency ^= mode
                assert frequency not in reached
                reached.add(frequency)
    return reached


def score_amplitude(score, q, ell):
    # Equal weights on all individual subset products before normalization.
    return sum((-1)**bad * comb(q - score, bad) * comb(score, t - bad)
               for t in range(ell + 1) for bad in range(t + 1))


def root_counts(q, k):
    # Count nonzero polys vanishing at exactly r of the q points by removing
    # those counted at larger sizes from every interpolation constraint.
    counts = [0] * k
    for j in reversed(range(k)):
        pairs = comb(q, j) * (q**(k - j) - 1)
        counts[j] = pairs - sum(comb(r, j) * counts[r] for r in range(j + 1, k))
    assert all(n >= 0 for n in counts) and sum(counts) == q**k - 1
    return counts


def check_fourier(b, modulus, k):
    field = Field(b, modulus)
    q, ell = field.q, k // 2
    n = q**k
    reached = frequency_support(field, k)
    size = sum(comb(q, t) * (q - 1)**t for t in range(ell + 1))
    balanced = sum(comb(q, t) for t in range(ell + 1))
    assert len(reached) == size
    values = [[evaluate(field, a, x, k) for x in range(q)] for a in range(n)]
    roots = Counter(row.count(0) for row in values[1:])
    assert [roots[r] for r in range(k)] == root_counts(q, k)
    rng = Random(325 + q)
    plant = rng.randrange(n)
    for forced in ([], [plant], [plant, plant ^ 1]):
        tables = []
        for x in range(q):
            prescribed = {values[a][x] for a in forced}
            others = [y for y in range(q) if y not in prescribed]
            tables.append(prescribed.union(rng.sample(others, q // 2 - len(prescribed))))
        scores = [sum(y in allowed for y, allowed in zip(row, tables)) for row in values]
        amplitude = [score_amplitude(s, q, ell) for s in scores]
        norm = sum(v*v for v in amplitude)
        assert norm == n * balanced
        for a in forced:
            assert scores[a] == q
            assert Fraction(amplitude[a]**2, norm) == Fraction(balanced, n)
        for threshold in range(q + 1):
            hits = [i for i, s in enumerate(scores) if s > threshold]
            mass = sum(amplitude[i]**2 for i in hits)
            assert mass * n <= len(hits) * balanced * norm <= len(hits) * size * norm
        walsh(amplitude)
        assert all(i in reached for i, a in enumerate(amplitude) if a)
    print(f"q={q}, k={k}, {n} polynomials, |R|={size}, B={balanced}; "
          "zero-, one-, and two-forced-plant tables checked")


def binomial_tail(n, threshold, p):
    """Exact probability that Bin(n,p) is strictly greater than threshold."""
    hits = p.numerator
    misses = p.denominator - hits
    numerator = sum(comb(n, i) * hits**i * misses**(n-i)
                    for i in range(max(0, threshold + 1), n + 1))
    return Fraction(numerator, p.denominator**n)


def check_random_family():
    k = 4
    q = k**4
    b = q.bit_length() - 1
    u = 1 + isqrt(q * k * b - 1)
    threshold = (q + k) // 2 + u
    assert threshold == 221 < q
    no_mean = q**k * binomial_tail(q, threshold, Fraction(1, 2))
    p = Fraction(q // 2 - 1, q - 1)
    wrong_mean = sum(count * binomial_tail(q-r, threshold-r, p)
                     for r, count in enumerate(root_counts(q, k)))
    for mean in (no_mean, wrong_mean):
        assert 0 < mean <= Fraction(1, q**k)
    print(f"q={q}, k={k}, T={threshold}; exact binomial sums give "
          f"E[NO witnesses]={float(no_mean):.6g}, "
          f"E[YES nonplants]={float(wrong_mean):.6g}")


if __name__ == "__main__":
    check_fourier(3, 0b1011, 4)
    check_fourier(4, 0b10011, 2)
    check_random_family()
