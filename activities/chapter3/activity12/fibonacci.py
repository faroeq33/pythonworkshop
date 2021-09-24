# We set the first 2 terms of the Fibonacci sequence here.
stored = {0: 0, 1: 1}


def fibonacci_dynamic(n):
    if n in stored:
        return stored[n]
    else:
        stored[n] = fibonacci_dynamic(n - 2) + fibonacci_dynamic(n - 1)
    return stored[n]


answer = fibonacci_dynamic(100)

print(answer)
