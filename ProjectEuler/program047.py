import itertools

def sqrt(x):
	assert x >= 0
	i = 1
	while i * i <= x:
		i *= 2
	y = 0
	while i > 0:
		if (y + i)**2 <= x:
			y += i
		i //= 2
	return y


def compute():
    cond = lambda i: all((count_distinct_prime_factors(i + j) == 4) for j in range(4))
    ans = next(filter(cond, itertools.count()))
    return str(ans)


def count_distinct_prime_factors(n):
    count = 0
    while n > 1:
        count += 1
        for i in range(2, sqrt(n) + 1):
            if n % i == 0:
                while True:
                    n //= i
                    if n % i != 0:
                        break
                break
        else:
            break  # n is prime
    return count


if __name__ == "__main__":
    print(compute())
