import fractions, itertools

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
	TARGET = fractions.Fraction(1, 10)
	numprimes = 0
	for n in itertools.count(1, 2):
		for i in range(4):
			if is_prime(n * n - i * (n - 1)):
				numprimes += 1
		if n > 1 and fractions.Fraction(numprimes, n * 2 - 1) < TARGET:
			return str(n)


if __name__ == "__main__":
	print(compute())
