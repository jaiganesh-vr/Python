import itertools

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
	ans = next(itertools.filterfalse(test_goldbach, itertools.count(9, 2)))
	return str(ans)


def test_goldbach(n):
	if n % 2 == 0 or is_prime(n):
		return True
	for i in itertools.count(1):
		k = n - 2 * i * i
		if k <= 0:
			return False
		elif is_prime(k):
			return True


if __name__ == "__main__":
	print(compute())
