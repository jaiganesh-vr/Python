def compute():
	SIZE = 1001  # Must be odd
	ans = 1  # Special case for size 1
	ans += sum(4 * i * i - 6 * (i - 1) for i in range(3, SIZE + 1, 2))
	return str(ans)


if __name__ == "__main__":
	print(compute())
