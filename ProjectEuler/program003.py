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
    n = 600851475143
    while True:
        p = least_prime_factor(n)
        if p < n:
            n //= p
        else:
            return str(n)

def least_prime_factor(n):
    assert n >= 2
    for i in range(2,sqrt(n) + 1):
        if n % i == 0:
            return i
    return n


if __name__ == "__main__":
	print(compute())