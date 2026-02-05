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


def list_primality(n):
    # Sieve of Eratosthenes
    result = [True] * (n + 1)
    result[0] = result[1] = False
    for i in range(sqrt(n) + 1):
        if result[i]:
            for j in range(i * i, len(result), i):
                result[j] = False
    return result


def compute():
    ans = 0
    isprime = eulerlib.list_primality(999999)
    primes = eulerlib.list_primes(999999)
    consecutive = 0
    for i in range(len(primes)):
        sum = primes[i]
        consec = 1
        for j in range(i + 1, len(primes)):
            sum += primes[j]
            consec += 1
            if sum >= len(isprime):
                break
            if isprime[sum] and consec > consecutive:
                ans = sum
                consecutive = consec
    return str(ans)


if __name__ == "__main__":
    print(compute())
