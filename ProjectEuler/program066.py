import fractions, math

def is_square(x):
    if x < 0:
        return False
    y = sqrt(x)
    return y * y == x

def sqrt(x):
    assert x >= 0
    i = 1
    while i * i <= x:
        i *= 2
    y = 0
    while i > 0:
        if (y + i) ** 2 <= x:
            y += i
        i //= 2
    return y


def compute():
    ans = max((n for n in range(2, 1001) if (not is_square(n))),
              key=smallest_solution_x)
    return str(ans)


def smallest_solution_x(n):
    contfrac = sqrt_to_continued_fraction(n)
    temp = contfrac[0] + contfrac[1][: -1]

    val = fractions.Fraction(temp[-1], 1)
    for term in reversed(temp[: -1]):
        val = 1 / val + term

    if len(contfrac[1]) % 2 == 0:
        return val.numerator
    else:
        return val.numerator ** 2 + val.denominator ** 2 * n


def sqrt_to_continued_fraction(n):
    terms = []
    seen = {}
    val = QuadraticSurd(0, 1, 1, n)
    while True:
        seen[val] = len(seen)
        flr = val.floor()
        terms.append(flr)
        val = (val - QuadraticSurd(flr, 0, 1, val.d)).reciprocal()
        if val in seen:
            break
    split = seen[val]
    return (terms[: split], terms[split:])


class QuadraticSurd:

    def __init__(self, a, b, c, d):
        if c == 0:
            raise ValueError()

        # Simplify
        if c < 0:
            a = -a
            b = -b
            c = -c
        gcd = math.gcd(math.gcd(a, b), c)
        if gcd != 1:
            a //= gcd
            b //= gcd
            c //= gcd

        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __sub__(self, other):
        if self.d != other.d:
            raise ValueError()
        return QuadraticSurd(
            self.a * other.c - other.a * self.c,
            self.b * other.c - other.b * self.c,
            self.c * other.c,
            self.d)

    def reciprocal(self):
        return QuadraticSurd(
            -self.a * self.c,
            self.b * self.c,
            self.b * self.b * self.d - self.a * self.a,
            self.d)

    def floor(self):
        temp = eulerlib.sqrt(self.b * self.b * self.d)
        if self.b < 0:
            temp = -(temp + 1)
        temp += self.a
        if temp < 0:
            temp -= self.c - 1
        return temp // self.c

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b \
            and self.c == other.c and self.d == other.d

    def __ne__(self, other):
        return not (self == other)

    def __hash__(self):
        return hash(self.a) + hash(self.b) + hash(self.c) + hash(self.d)


if __name__ == "__main__":
    print(compute())
