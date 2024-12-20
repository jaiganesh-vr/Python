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
    TARGET = 2000000
    end = sqrt(TARGET) + 1
    gen = ((w, h) for w in range(1, end) for h in range(1, end))
    func = lambda wh: abs(num_rectangles(*wh) - TARGET)
    ans = min(gen, key=func)
    return str(ans[0] * ans[1])


def num_rectangles(m, n):
    return (m + 1) * m * (n + 1) * n // 4  # A bit more than m^2 n^2 / 4


if __name__ == "__main__":
    print(compute())
