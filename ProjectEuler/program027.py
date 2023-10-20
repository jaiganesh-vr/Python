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

def is_prime1(x):
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
	ans = max(((a, b) for a in range(-999, 1000) for b in range(2, 1000)),
		key=count_consecutive_primes)
	return str(ans[0] * ans[1])


def count_consecutive_primes(ab):
	a, b = ab
	for i in itertools.count():
		n = i * i + i * a + b
		if not is_prime(n):
			return i


isprimecache = list_primality(1000)

def is_prime(n):
	if n < 0:
		return False
	elif n < len(isprimecache):
		return isprimecache[n]
	else:
		return is_prime1(n)


if __name__ == "__main__":
	print(compute())
