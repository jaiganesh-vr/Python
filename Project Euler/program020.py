import math

def compute():
	n = math.factorial(100)
	ans = sum(int(c) for c in str(n))
	return str(ans)

if __name__ == "__main__":
	print(compute())
