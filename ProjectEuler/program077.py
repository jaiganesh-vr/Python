import itertools
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
def is_prime(x):
    if x <= 1:
        return False
    elif x <= 3:
        return True
    elif x % 2 == 0:
        return False
    else:
        for i in range(3, sqrt(x) + 1, 2):
            if x % i == 0:
                return False
        return True
def compute():
    cond = lambda n: num_prime_sum_ways(n) > 5000
    ans = next(filter(cond, itertools.count(2)))
    return str(ans)


primes = [2]
def num_prime_sum_ways(n):
    for i in range(primes[-1] + 1, n + 1):
        if is_prime(i):
            primes.append(i)

    ways = [1] + [0] * n
    for p in primes:
        for i in range(n + 1 - p):
            ways[i + p] += ways[i]
    return ways[n]

if __name__ == "__main__":
    print(compute())
