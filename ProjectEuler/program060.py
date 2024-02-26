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


def list_primality(n):
    # Sieve of Eratosthenes
    result = [True] * (n + 1)
    result[0] = result[1] = False
    for i in range(sqrt(n) + 1):
        if result[i]:
            for j in range(i * i, len(result), i):
                result[j] = False
    return result

def is_square(x):
	if x < 0:
		return False
	y = sqrt(x)
	return y * y == x

def list_primes(n):
	return [i for (i, isprime) in enumerate(list_primality(n)) if isprime]

def compute():
    PRIME_LIMIT = 100000  # Arbitrary initial cutoff
    primes = list_primes(PRIME_LIMIT)

    def find_set_sum(prefix, targetsize, sumlimit):
        if len(prefix) == targetsize:
            return sum(primes[i] for i in prefix)
        else:
            istart = 0 if (len(prefix) == 0) else (prefix[-1] + 1)
            for i in range(istart, len(primes)):
                if primes[i] > sumlimit:
                    break
                if all((is_concat_prime(i, j) and is_concat_prime(j, i)) for j in prefix):
                    prefix.append(i)
                    result = find_set_sum(prefix, targetsize, sumlimit - primes[i])
                    prefix.pop()
                    if result is not None:
                        return result
            return None

    # Tests whether concat(primes[x], primes[y]) is a prime number, with memoization.
    @eulerlib.memoize
    def is_concat_prime(x, y):
        return is_prime(int(str(primes[x]) + str(primes[y])))

    # Tests whether the given integer is prime. The implementation performs trial division,
    # first using the list of primes named 'primes', then switching to simple incrementation.
    # This requires the last number in 'primes' (if any) to be an odd number.
    def is_prime(x):
        if x < 0:
            raise ValueError()
        elif x in (0, 1):
            return False
        else:
            end = sqrt(x)
            for p in primes:
                if p > end:
                    break
                if x % p == 0:
                    return False
            for i in range(primes[-1] + 2, end + 1, 2):
                if x % i == 0:
                    return False
            return True

    sumlimit = PRIME_LIMIT
    while True:
        setsum = find_set_sum([], 5, sumlimit - 1)
        if setsum is None:  # No smaller sum found
            return str(sumlimit)
        sumlimit = setsum


if __name__ == "__main__":
    print(compute())
