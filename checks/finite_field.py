"""Binary extension field arithmetic and in-place Walsh transform for the checks."""


class Field:
    def __init__(self, b, modulus):
        self.b = b
        self.q = 1 << b
        self.modulus = modulus
        self.trace = [self.absolute_trace(x) for x in range(self.q)]

    def mul(self, x, y):
        result = 0
        while y:
            if y & 1:
                result ^= x
            y >>= 1
            x <<= 1
            if x & self.q:
                x ^= self.modulus
        return result

    def power(self, x, degree):
        result = 1
        while degree:
            if degree & 1:
                result = self.mul(result, x)
            x = self.mul(x, x)
            degree >>= 1
        return result

    def absolute_trace(self, x):
        value = 0
        for _ in range(self.b):
            value ^= x
            x = self.mul(x, x)
        assert value in (0, 1)
        return value


def walsh(values):
    width = 1
    while width < len(values):
        for start in range(0, len(values), width * 2):
            for i in range(start, start + width):
                lower, upper = values[i], values[i + width]
                values[i], values[i + width] = lower + upper, lower - upper
        width *= 2
