import itertools

def compute():
    DIGITS = 1000
    prev = 1
    cur = 0
    for i in itertools.count():
        # At this point, prev = fibonacci(i - 1) and cur = fibonacci(i)
        if len(str(cur)) > DIGITS:
            raise RuntimeError("Not found")
        elif len(str(cur)) == DIGITS:
            return str(i)

        # Advance the Fibonacci sequence by one step
        prev, cur = cur, prev + cur


if __name__ == "__main__":
    print(compute())
