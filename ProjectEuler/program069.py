import fractions

def list_totients(n):
	result = list(range(n + 1))
	for i in range(2, len(result)):
		if result[i] == i:  # i is prime
			for j in range(i, len(result), i):
				result[j] -= result[j] // i
	return result

def compute():
	totients = list_totients(10**6)
	ans = max(range(2, len(totients)), key=(lambda i: fractions.Fraction(i, totients[i])))
	return str(ans)


if __name__ == "__main__":
	print(compute())
