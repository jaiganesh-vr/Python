def list_totients(n):
	result = list(range(n + 1))
	for i in range(2, len(result)):
		if result[i] == i:  # i is prime
			for j in range(i, len(result), i):
				result[j] -= result[j] // i
	return result

def compute():
	totients = list_totients(10**7 - 1)
	minnumer = 1
	mindenom = 0
	for (i, tot) in enumerate(totients[2 : ], 2):
		if i * mindenom < minnumer * tot and sorted(str(i)) == sorted(str(tot)):
			minnumer = i
			mindenom = totients[i]
	return str(minnumer)


if __name__ == "__main__":
	print(compute())
