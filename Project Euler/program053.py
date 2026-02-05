import math


def binomial(n, k):
    assert 0 <= k <= n
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def compute():
    ans = sum(1
              for n in range(1, 101)
              for k in range(0, n + 1)
              if binomial(n, k) > 1000000)
    return str(ans)


if __name__ == "__main__":
    print(compute())
