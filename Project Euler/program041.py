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
	# Note: The only 1-digit pandigital number is 1, which is not prime. Thus we require n >= 2.
	for n in reversed(range(2, 10)):
		arr = list(reversed(range(1, n + 1)))
		while True:
			if arr[-1] not in NONPRIME_LAST_DIGITS:
				n = int("".join(str(x) for x in arr))
				if is_prime(n):
					return str(n)
			if not prev_permutation(arr):
				break
	raise AssertionError()

NONPRIME_LAST_DIGITS = {0, 2, 4, 5, 6, 8}


def prev_permutation(arr):
	i = len(arr) - 1
	while i > 0 and arr[i - 1] <= arr[i]:
		i -= 1
	if i <= 0:
		return False
	j = len(arr) - 1
	while arr[j] >= arr[i - 1]:
		j -= 1
	arr[i - 1], arr[j] = arr[j], arr[i - 1]
	arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
	return True


if __name__ == "__main__":
	print(compute())