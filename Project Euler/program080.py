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
    DIGITS = 100
    MULTIPLIER = 100 ** DIGITS
    ans = sum(
        sum(int(c) for c in str(sqrt(i * MULTIPLIER))[: DIGITS])
        for i in range(100)
        if sqrt(i) ** 2 != i)
    return str(ans)


if __name__ == "__main__":
    print(compute())
